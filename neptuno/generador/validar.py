# Valida los .md de content/ contra las reglas del BRIEF_BASE_NEPTUNO y los compila a .docx.
# Uso: python3 validar.py [content/CODIGO.md ...]   (sin argumentos: todos)
import os, re, sys, glob, json, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
H1_PR = ['OBJETIVO', 'ALCANCE', 'DEFINICIONES', 'LOCALIZACIÓN', 'REFERENCIAS', 'RESPONSABILIDADES', 'RECURSOS',
         'DESARROLLO DE LA ACTIVIDAD', 'ASPECTOS SST (HSE)', 'ANÁLISIS DE TRABAJO SEGURO (ATS)',
         'ASPECTOS AMBIENTALES', 'ATENCIÓN DE EMERGENCIAS', 'REGISTROS', 'ANEXOS', 'CONTROL DE CAMBIOS']
# Nombres propios de terceros que no pueden aparecer en un documento base (fabricantes, operadores, clientes).
MARCAS = r'\b(SMA|Huawei|Sungrow|Ingeteam|Power Electronics|SolarEdge|Fronius|ABB|Siemens|Schneider|Hitachi|' \
         r'Nextracker|Array Technologies|Soltec|PV Hardware|Arctech|First Solar|Jinko|JinkoSolar|LONGi|Trina|Canadian Solar|' \
         r'JA Solar|Risen|Staubli|Stäubli|Amphenol|Prysmian|Nexans|Centelsa|Procables|3M|Raychem|TE Connectivity|Cellpack|' \
         r'Fluke|Megger|HT Italia|Seaward|Metrel|Kyoritsu|Hioki|Chauvin|FLIR|Teledyne|Testo|Caterpillar|Liebherr|Tadano|Grove|' \
         r'Manitowoc|JLG|Genie|Haulotte|Cadweld|Erico|nVent|Thermoweld|Furse|Ecopetrol|ISA|EPM|Celsia|Enel|Codensa|Air-e|' \
         r'Afinia|Essa|CHEC|Cedenar|Electrohuila|haboquet|boquet|ELNR|studocu)\b'

def check(path):
    errs, warns = [], []
    t = open(path, encoding='utf-8').read()
    code = os.path.splitext(os.path.basename(path))[0]
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.S)
    if not m:
        return ['sin YAML'], warns
    meta = dict((k.strip(), v.strip()) for k, v in (l.split(':', 1) for l in m.group(1).splitlines() if ':' in l))
    for k in ('code', 'header_title', 'cover_title', 'cover_subtitle'):
        if not meta.get(k):
            errs.append(f'YAML sin {k}')
    if meta.get('code') != code:
        errs.append(f'code YAML ({meta.get("code")}) distinto del nombre de archivo ({code})')
    ht = meta.get('header_title', '')
    if len(ht) > 55: errs.append(f'header_title > 55 caracteres ({len(ht)})')
    if ht != ht.upper(): errs.append('header_title no está en mayúsculas')
    body = t[m.end():]
    lines = body.splitlines()
    h1 = [re.sub(r'^\d+\.\s*', '', l[2:].strip()) for l in lines if l.startswith('# ')]
    if '-PR-' in code:
        if h1 != H1_PR:
            errs.append(f'H1 no coinciden con la estructura de 15 numerales: {h1}')
    # tablas
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('|'):
            start = i; blk = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                blk.append(lines[i].strip()); i += 1
            if len(blk) < 2 or not re.match(r'^\|(\s*:?-{2,}:?\s*\|)+$', blk[1]):
                errs.append(f'tabla sin línea separadora |---| (línea {start + 1 + t[:m.end()].count(chr(10))})')
            ncols = len(blk[0].strip('|').split('|'))
            if ncols > 7: errs.append(f'tabla con {ncols} columnas (máx. 7), línea {start + 1}')
            for r in blk:
                if not r.endswith('|'): errs.append(f'fila de tabla sin | final: {r[:60]}')
                if len(r.strip('|').split('|')) != ncols and not re.match(r'^\|(\s*:?-{2,}:?\s*\|)+$', r):
                    warns.append(f'fila con distinto n.º de columnas ({ncols}): {r[:70]}')
        else:
            i += 1
    # formato no permitido
    for n, l in enumerate(lines, 1):
        if re.search(r'\]\(|!\[|<(?!br\s*/?>)[a-zA-Z/]', l): errs.append(f'enlace/imagen/HTML en línea {n}: {l[:70]}')
        if re.search(r'(?<![\*\w])\*(?!\*)[^*\n]+\*(?!\*)|(?<![\w\[])_[^_\s][^_]*_(?![\w\]])', l) and not l.strip().startswith('|'):
            warns.append(f'posible cursiva en línea {n}: {l[:70]}')
        if l.startswith('#') and not re.match(r'^#{1,4} ', l): errs.append(f'encabezado mal formado línea {n}')
    for mm in re.finditer(MARCAS, body, re.I):
        errs.append(f'nombre propio de tercero: "{mm.group(0)}" (pos {mm.start()})')
    if 'GameChange' in body and '-OPE-PR-0' in code and int(code[-3:]) >= 15:
        warns.append('cita GameChange: permitido solo como tracker de referencia, marcado como tal')
    fmt = re.findall(r'^#{2,4}\s+(NES-[A-Z]{3}-F-\d{3})\s*[—–-]', body, re.M)
    return errs, warns, fmt

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, 'content', '*.md')))
    allfmt = {}; bad = 0
    for f in files:
        r = check(f)
        errs, warns = r[0], r[1]
        fmt = r[2] if len(r) > 2 else []
        for c in fmt:
            allfmt.setdefault(c, []).append(os.path.basename(f))
        print(('ERR ' if errs else 'OK  ') + os.path.basename(f) + f'  formatos={fmt}')
        for e in errs: print('   ✗', e)
        for w in warns[:15]: print('   !', w)
        if errs: bad += 1
    for c, fs in allfmt.items():
        if len(fs) > 1: print('   ✗ código de formato repetido', c, fs); bad += 1
    if not bad:
        out = subprocess.run([sys.executable, os.path.join(HERE, 'build_neptuno.py')] + files, capture_output=True, text=True)
        print(out.stdout[-3000:], out.stderr[-3000:])
    sys.exit(1 if bad else 0)
