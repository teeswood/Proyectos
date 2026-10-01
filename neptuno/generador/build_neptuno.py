# Generador de procedimientos BASE de Neptuno Energy Services: content/<CODE>.md -> out/<archivo>.docx
# Documentos base, sin cliente ni obra: se aterrizan reemplazando [CONTRATISTA], [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio].
# Generador propio de Neptuno Energy Services.
import os, re, sys, glob, copy, json
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'brand', 'logo_neptuno_navy.png')      # encabezado, fondo claro
LOGO_BLANCO = os.path.join(HERE, 'brand', 'logo_neptuno_blanco.png')  # portada, banda azul

# Identidad Neptuno Energy Services (extraída de su portafolio corporativo)
NAVY = '211B3B'        # azul noche (principal)
GOLD = '4EC99B'        # verde agua (acento: filetes, viñetas)
GOLD_DARK = '0F7355'   # verde agua oscuro legible (títulos nivel 3, etiquetas NOTA)
GOLD_TINT = 'E9F7F1'   # tinte verde (notas)
NAVY_TINT = 'EDEDF3'   # tinte azul (tablas)
YELLOW = 'A6CEED'      # azul claro (código en la banda de portada)
GREY = '595959'
TEXT = '262626'
BORDER = 'C2C3D0'
FONT = 'Arial'
AUTHOR = 'Neptuno Energy Services'
EMPRESA = 'Neptuno Energy Services'

PROJECT = 'Documento base · aplicable a proyectos fotovoltaicos'
CLIENT_LINE = 'Ejecuta: Neptuno Energy Services  ·  Cliente: [CLIENTE]  ·  Propietario: [PROPIETARIO]'
CONTRACT_LINE = 'Proyecto: [PROYECTO]  ·  Contrato N.º: [__________]'
DATE = '25-09-2026'
REV = '01'
FOOTER_1 = 'Neptuno Energy Services  ·  NIT 901.744.411-5'
FOOTER_2 = 'Documento base. Copia no controlada una vez impresa.'
PROPERTY = ('Documento base propiedad de Neptuno Energy Services. Se entrega para su adaptación al proyecto '
            'indicado; se prohíbe su reproducción o entrega a terceros sin autorización escrita.')

FILENAMES = {
    'NES-OPE-PR-001': 'NES-OPE-PR-001_Topografia_y_Control_Topografico_V01',
    'NES-OPE-PR-002': 'NES-OPE-PR-002_Excavacion_de_Zanjas_y_Movimiento_de_Tierras_V01',
    'NES-OPE-PR-003': 'NES-OPE-PR-003_Logistica_de_Componentes_de_Tracker_V01',
    'NES-OPE-PR-004': 'NES-OPE-PR-004_Replanteo_e_Hincado_de_Perfiles_V01',
    'NES-OPE-PR-005': 'NES-OPE-PR-005_Pruebas_de_Arrancamiento_Pull_Out_Test_V01',
    'NES-OPE-PR-006': 'NES-OPE-PR-006_Reparacion_de_Hincas_V01',
    'NES-OPE-PR-007': 'NES-OPE-PR-007_Method_Statement_de_Hincado_y_Estructura_V01',
    'NES-OPE-PR-008': 'NES-OPE-PR-008_Montaje_de_Componentes_de_Tracker_V01',
    'NES-OPE-PR-009': 'NES-OPE-PR-009_Montaje_de_Estructuras_Metalicas_V01',
    'NES-OPE-PR-010': 'NES-OPE-PR-010_Montaje_y_Sustitucion_de_Modulos_FV_V01',
    'NES-OPE-PR-011': 'NES-OPE-PR-011_Preservacion_de_Materiales_de_Puesta_a_Tierra_V01',
    'NES-CAL-PLN-001': 'NES-CAL-PLN-001_Plan_de_Inspeccion_y_Ensayos_Mecanico_V01',
    'NES-SST-PLN-001': 'NES-SST-PLN-001_Plan_de_Prevencion_Preparacion_y_Respuesta_ante_Emergencias_V01',
}
# Nombres de archivo de los documentos nuevos (biblioteca ampliada)
_extra = os.path.join(HERE, 'nombres_archivo.json')
if os.path.exists(_extra):
    FILENAMES.update(json.load(open(_extra, encoding='utf-8')))

# ---------------------------------------------------------------- utilidades XML
def el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn(k), str(v))
    return e

def set_cell_fill(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn('w:shd')):
        tcPr.remove(old)
    tcPr.append(el('w:shd', **{'w:val': 'clear', 'w:color': 'auto', 'w:fill': fill}))

def set_cell_borders(cell, **sides):
    """sides: top/left/bottom/right = (val, sz, color) o None para 'nil'."""
    tcPr = cell._tc.get_or_add_tcPr()
    b = tcPr.find(qn('w:tcBorders'))
    if b is None:
        b = el('w:tcBorders'); tcPr.append(b)
    for side in ('top', 'left', 'bottom', 'right'):
        if side in sides:
            for old in b.findall(qn('w:' + side)):
                b.remove(old)
            spec = sides[side]
            if spec is None:
                b.append(el('w:' + side, **{'w:val': 'nil'}))
            else:
                val, sz, color = spec
                b.append(el('w:' + side, **{'w:val': val, 'w:sz': sz, 'w:space': 0, 'w:color': color}))

def set_cell_margins(cell, top=50, left=90, bottom=50, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    m = el('w:tcMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        m.append(el('w:' + k, **{'w:w': v, 'w:type': 'dxa'}))
    tcPr.append(m)

def set_table_borders(tbl, color=BORDER, sz=4, inside=True):
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(old)
    b = el('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right') + (('insideH', 'insideV') if inside else ()):
        b.append(el('w:' + side, **{'w:val': 'single', 'w:sz': sz, 'w:space': 0, 'w:color': color}))
    if not inside:
        for side in ('insideH', 'insideV'):
            b.append(el('w:' + side, **{'w:val': 'nil'}))
    tblPr.append(b)

def set_table_widths(tbl, widths):
    tbl.autofit = False
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn('w:tblW')):
        tblPr.remove(old)
    tblPr.append(el('w:tblW', **{'w:w': sum(widths), 'w:type': 'dxa'}))
    lay = el('w:tblLayout', **{'w:type': 'fixed'}); tblPr.append(lay)
    grid = tbl._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn('w:gridCol'))):
        gc.set(qn('w:w'), str(widths[i]))
    for row in tbl.rows:
        for i, c in enumerate(row.cells):
            tcPr = c._tc.get_or_add_tcPr()
            for old in tcPr.findall(qn('w:tcW')):
                tcPr.remove(old)
            tcPr.insert(0, el('w:tcW', **{'w:w': widths[i], 'w:type': 'dxa'}))

def row_no_split(row, header=False):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(el('w:cantSplit'))
    if header:
        trPr.append(el('w:tblHeader'))

def para_border(p, side, color, sz, space=2, val='single'):
    pPr = p._p.get_or_add_pPr()
    b = pPr.find(qn('w:pBdr'))
    if b is None:
        b = el('w:pBdr'); pPr.append(b)
    b.append(el('w:' + side, **{'w:val': val, 'w:sz': sz, 'w:space': space, 'w:color': color}))

def add_field(paragraph, instr, size=None, bold=False, color=None):
    def mk(r_children):
        r = OxmlElement('w:r')
        rPr = OxmlElement('w:rPr')
        if bold: rPr.append(el('w:b'))
        if color: rPr.append(el('w:color', **{'w:val': color}))
        if size:
            rPr.append(el('w:sz', **{'w:val': int(size * 2)})); rPr.append(el('w:szCs', **{'w:val': int(size * 2)}))
        r.append(rPr)
        for ch in r_children: r.append(ch)
        paragraph._p.append(r)
    mk([el('w:fldChar', **{'w:fldCharType': 'begin'})])
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = f' {instr} '
    mk([it])
    mk([el('w:fldChar', **{'w:fldCharType': 'separate'})])
    t = OxmlElement('w:t'); t.text = '1'
    mk([t])
    mk([el('w:fldChar', **{'w:fldCharType': 'end'})])

def run(p, text, size=None, bold=False, color=None, italic=False, font=None):
    r = p.add_run(text)
    if size: r.font.size = Pt(size)
    r.bold = bold or None
    if italic: r.italic = True
    if color: r.font.color.rgb = RGBColor.from_string(color)
    if font: r.font.name = font
    return r

def add_inline(p, text, size=None, color=None, base_bold=False):
    """Texto con **negritas** y <br> como salto de línea."""
    parts = re.split(r'(\*\*[^*]+\*\*)', text)
    for part in parts:
        if not part:
            continue
        bold = base_bold
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            part = part[2:-2]; bold = True
        segs = re.split(r'<br\s*/?>', part)
        for i, seg in enumerate(segs):
            if i > 0:
                p.add_run().add_break()
            if seg:
                run(p, seg, size=size, bold=bold, color=color)

def pfmt(p, before=0, after=4, align=None, keep_next=False, line=None):
    pf = p.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if align is not None: pf.alignment = align
    if keep_next: pf.keep_with_next = True
    if line: pf.line_spacing = line

# ---------------------------------------------------------------- estilos
def strip_theme_fonts(rPr):
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = el('w:rFonts'); rPr.insert(0, rf)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(a)) is not None:
            del rf.attrib[qn(a)]
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), FONT)

def setup_styles(doc):
    st = doc.styles
    # docDefaults
    dd = doc.styles.element.find(qn('w:docDefaults'))
    rPr = dd.find(qn('w:rPrDefault')).find(qn('w:rPr'))
    strip_theme_fonts(rPr)
    lang = rPr.find(qn('w:lang'))
    if lang is None:
        lang = el('w:lang'); rPr.append(lang)
    lang.set(qn('w:val'), 'es-CO'); lang.set(qn('w:eastAsia'), 'es-CO'); lang.set(qn('w:bidi'), 'ar-SA')
    for s in st:
        e = s.element.find(qn('w:rPr'))
        if e is not None and e.find(qn('w:rFonts')) is not None:
            strip_theme_fonts(e)
    normal = st['Normal']
    normal.font.name = FONT; normal.font.size = Pt(9.5)
    normal.font.color.rgb = RGBColor.from_string(TEXT)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.1
    spec = {
        'Heading 1': (11.5, True, False, NAVY, 16, 6),
        'Heading 2': (10.5, True, False, NAVY, 10, 4),
        'Heading 3': (10, True, False, TEXT, 8, 3),
        'Heading 4': (9.5, True, True, '404040', 6, 2),
    }
    for name, (size, b, it, color, bef, aft) in spec.items():
        s = st[name]
        s.font.name = FONT; s.font.size = Pt(size); s.font.bold = b; s.font.italic = it
        s.font.color.rgb = RGBColor.from_string(color)
        s.paragraph_format.space_before = Pt(bef); s.paragraph_format.space_after = Pt(aft)
        s.paragraph_format.keep_with_next = True
        s.paragraph_format.line_spacing = 1.0
        strip_theme_fonts(s.element.get_or_add_rPr())
        # quitar colores de tema del estilo base
        c = s.element.rPr.find(qn('w:color'))
        for a in ('w:themeColor', 'w:themeShade', 'w:themeTint'):
            if c is not None and c.get(qn(a)) is not None:
                del c.attrib[qn(a)]
    for n in ('TOC 1', 'TOC 2'):
        try:
            s = st[n]
        except KeyError:
            s = st.add_style(n, 1)
            s.base_style = st['Normal']
        s.font.name = FONT
        s.font.size = Pt(9.5 if n == 'TOC 1' else 9)
        s.font.bold = (n == 'TOC 1')
        s.font.color.rgb = RGBColor.from_string(NAVY if n == 'TOC 1' else TEXT)
        s.paragraph_format.space_before = Pt(4 if n == 'TOC 1' else 0)
        s.paragraph_format.space_after = Pt(2)
        s.paragraph_format.left_indent = Inches(0 if n == 'TOC 1' else 0.25)

# ---------------------------------------------------------------- numeración
class Numbering:
    BUL, DEC = 90, 91
    def __init__(self, doc):
        self.np = doc.part.numbering_part.element
        first_num = self.np.find(qn('w:num'))
        for absn in (self._bullet(), self._decimal()):
            if first_num is not None:
                first_num.addprevious(absn)
            else:
                self.np.append(absn)
        self.next_id = 900
        self.bullet_id = self._new_num(self.BUL, restart=False)

    def _lvl(self, ilvl, fmt, text, left, hanging, color, bold=False):
        l = el('w:lvl', **{'w:ilvl': ilvl})
        l.append(el('w:start', **{'w:val': 1}))
        l.append(el('w:numFmt', **{'w:val': fmt}))
        l.append(el('w:lvlText', **{'w:val': text}))
        l.append(el('w:lvlJc', **{'w:val': 'left'}))
        pPr = el('w:pPr'); pPr.append(el('w:ind', **{'w:left': left, 'w:hanging': hanging})); l.append(pPr)
        rPr = el('w:rPr'); rPr.append(el('w:rFonts', **{'w:ascii': FONT, 'w:hAnsi': FONT, 'w:hint': 'default'}))
        if bold: rPr.append(el('w:b'))
        rPr.append(el('w:color', **{'w:val': color})); l.append(rPr)
        return l

    def _bullet(self):
        a = el('w:abstractNum', **{'w:abstractNumId': self.BUL})
        a.append(el('w:multiLevelType', **{'w:val': 'hybridMultilevel'}))
        a.append(self._lvl(0, 'bullet', '■', 340, 230, GOLD))
        a.append(self._lvl(1, 'bullet', '–', 700, 230, NAVY))
        a.append(self._lvl(2, 'bullet', '·', 1060, 230, NAVY))
        return a

    def _decimal(self):
        a = el('w:abstractNum', **{'w:abstractNumId': self.DEC})
        a.append(el('w:multiLevelType', **{'w:val': 'hybridMultilevel'}))
        a.append(self._lvl(0, 'decimal', '%1.', 360, 300, NAVY, bold=True))
        a.append(self._lvl(1, 'lowerLetter', '%2)', 720, 280, NAVY))
        return a

    def _new_num(self, absid, restart=True):
        nid = self.next_id; self.next_id += 1
        n = el('w:num', **{'w:numId': nid})
        n.append(el('w:abstractNumId', **{'w:val': absid}))
        if restart:
            o = el('w:lvlOverride', **{'w:ilvl': 0}); o.append(el('w:startOverride', **{'w:val': 1})); n.append(o)
        self.np.append(n)
        return nid

    def new_decimal(self):
        return self._new_num(self.DEC)

def set_num(p, num_id, ilvl=0):
    pPr = p._p.get_or_add_pPr()
    numPr = el('w:numPr')
    numPr.append(el('w:ilvl', **{'w:val': ilvl}))
    numPr.append(el('w:numId', **{'w:val': num_id}))
    pPr.insert(0, numPr) if pPr.find(qn('w:pStyle')) is None else pPr.find(qn('w:pStyle')).addnext(numPr)

# ---------------------------------------------------------------- tablas
TABLE_W = 9360

def col_widths(rows, ncols, total=TABLE_W):
    scores = []
    for i in range(ncols):
        lens = [len(re.sub(r'\*\*|<br\s*/?>', ' ', r[i])) for r in rows if i < len(r)]
        if not lens:
            scores.append(4); continue
        mx = max(lens); mean = sum(lens) / len(lens)
        s = 0.45 * min(mx, 90) + 0.55 * min(mean, 90)
        scores.append(max(s, 3.5))
    minw = 620 if ncols >= 6 else 800
    raw = [s / sum(scores) * total for s in scores]
    # ancho mínimo para no partir palabras (token más largo de la columna, tope 1400 dxa)
    per_char = 95 if ncols >= 6 else 110
    tok_min = []
    for i in range(ncols):
        toks = [tk for r in rows if i < len(r) for tk in re.split(r'[\s/]+|<br\s*/?>', r[i].replace('**', '')) if tk]
        longest = max((len(tk) for tk in toks), default=3)
        tok_min.append(min(1400, longest * per_char + 200))
    mins = [max(minw, tok_min[i]) for i in range(ncols)]
    if sum(mins) > total:
        mins = [m * total / sum(mins) for m in mins]
    w = [max(mins[i], x) for i, x in enumerate(raw)]
    excess = sum(w) - total
    if excess > 0:
        big = [i for i in range(ncols) if w[i] > mins[i]]
        tot_big = sum(w[i] - mins[i] for i in big)
        for i in big:
            w[i] -= excess * (w[i] - mins[i]) / tot_big
    w = [int(round(x)) for x in w]
    w[-1] += total - sum(w)
    return w

def add_table(doc, rows, plain=False):
    ncols = max(len(r) for r in rows)
    rows = [r + [''] * (ncols - len(r)) for r in rows]
    fs = 8.5 if ncols <= 5 else (8 if ncols == 6 else 7.5)
    t = doc.add_table(rows=len(rows), cols=ncols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t)
    set_table_widths(t, col_widths(rows, ncols))
    for ri, r in enumerate(rows):
        hdr = (ri == 0 and not plain)
        row_no_split(t.rows[ri], header=hdr)
        for ci, txt in enumerate(r):
            c = t.cell(ri, ci)
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(c)
            p = c.paragraphs[0]; pfmt(p, 0, 0, line=1.0)
            if hdr:
                set_cell_fill(c, NAVY)
                add_inline(p, txt.replace('**', ''), size=fs, color='FFFFFF', base_bold=True)
            else:
                if not plain and ri % 2 == 0:
                    set_cell_fill(c, NAVY_TINT)
                add_inline(p, txt, size=fs)
                if plain and re.match(r'^[^\[]{1,40}:', txt.strip()) is None and ci == 0 and txt.strip() in (
                        'Empresa', 'Nombre', 'Cargo', 'Firma', 'Fecha'):
                    for rr in p.runs: rr.bold = True
    sp = doc.add_paragraph(); pfmt(sp, 0, 2)
    return t

def add_callout(doc, text):
    m = re.match(r'^(NOTA|ALTO|IMPORTANTE|ADVERTENCIA|PRECAUCIÓN)\s*:\s*(.*)$', text, re.S)
    kind, body = (m.group(1), m.group(2)) if m else ('NOTA', text)
    critical = kind in ('ALTO', 'ADVERTENCIA', 'PRECAUCIÓN')
    fill, bar, lab = ('FCEBEA', 'C0392B', 'B03A2E') if critical else (GOLD_TINT, GOLD, TEXT)
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_widths(t, [TABLE_W])
    c = t.cell(0, 0)
    set_cell_fill(c, fill)
    set_cell_borders(c, top=None, bottom=None, right=None, left=('single', 36, bar))
    set_cell_margins(c, 80, 160, 80, 120)
    row_no_split(t.rows[0])
    p = c.paragraphs[0]; pfmt(p, 0, 0)
    run(p, kind + ': ', size=9, bold=True, color=lab)
    add_inline(p, body.strip(), size=9)
    sp = doc.add_paragraph(); pfmt(sp, 0, 2)

# ---------------------------------------------------------------- encabezado / pie / portada
def logo_run(p, width_in):
    p.add_run().add_picture(LOGO, width=Inches(width_in))

def build_header(section, meta):
    h = section.header
    h.is_linked_to_previous = False
    p0 = h.paragraphs[0]
    t = h.add_table(rows=1, cols=3, width=Inches(6.5))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t, color=NAVY, sz=6)
    set_table_widths(t, [2150, 4910, 2300])
    c0, c1, c2 = t.rows[0].cells
    for c in (c0, c1, c2):
        c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_margins(c, 50, 80, 50, 80)
    p = c0.paragraphs[0]; pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER); logo_run(p, 1.15)
    p = c1.paragraphs[0]; pfmt(p, 0, 2, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, meta['header_title'], size=8.5, bold=True, color=NAVY)
    p = c1.add_paragraph(); pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, PROJECT, size=7.5, color=GREY)
    set_cell_fill(c2, NAVY_TINT)
    lines = [('Código: ', meta['code']), ('Versión: ', REV), ('Fecha: ', DATE)]
    p = c2.paragraphs[0]
    for i, (k, v) in enumerate(lines):
        if i: p = c2.add_paragraph()
        pfmt(p, 0, 0, line=1.0)
        run(p, k, size=7.5, bold=True, color=NAVY); run(p, v, size=7.5)
    # mover la tabla antes del párrafo inicial y usar ese párrafo como filete dorado
    p0._p.addprevious(t._tbl)
    pfmt(p0, 0, 0, line=1.0)
    r = p0.add_run(''); r.font.size = Pt(2)

def build_footer(footer):
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    pfmt(p, 0, 1, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, 'Página ', size=8, color=TEXT); add_field(p, 'PAGE', size=8); run(p, ' de ', size=8); add_field(p, 'NUMPAGES', size=8)
    p2 = footer.add_paragraph(); pfmt(p2, 0, 0, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p2, FOOTER_1 + '  ·  ', size=6.5, bold=True, color=NAVY); run(p2, FOOTER_2, size=6.5, color=GREY)

def build_cover(doc, meta):
    p = doc.paragraphs[0] if doc.paragraphs else doc.add_paragraph()
    pfmt(p, 30, 10, WD_ALIGN_PARAGRAPH.CENTER)
    # banda azul con el logo blanco y el título
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_widths(t, [TABLE_W])
    c = t.cell(0, 0); set_cell_fill(c, NAVY)
    set_cell_borders(c, top=None, left=None, right=None, bottom=('single', 36, GOLD))
    set_cell_margins(c, 320, 360, 300, 360)
    p = c.paragraphs[0]; pfmt(p, 0, 14, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    p.add_run().add_picture(LOGO_BLANCO, width=Inches(3.5))
    p = c.add_paragraph(); pfmt(p, 0, 6, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, meta['code'] + '  ·  VERSIÓN ' + REV + '  ·  DOCUMENTO BASE', size=10, bold=True, color=YELLOW)
    p = c.add_paragraph(); pfmt(p, 0, 6, WD_ALIGN_PARAGRAPH.CENTER, line=1.05)
    run(p, meta['cover_title'], size=19, bold=True, color='FFFFFF')
    p = c.add_paragraph(); pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, meta['cover_subtitle'], size=11, color='FFFFFF')
    # datos de proyecto
    p = doc.add_paragraph(); pfmt(p, 26, 4, WD_ALIGN_PARAGRAPH.CENTER)
    run(p, PROJECT.upper(), size=12.5, bold=True, color=NAVY)
    p = doc.add_paragraph(); pfmt(p, 0, 2, WD_ALIGN_PARAGRAPH.CENTER)
    run(p, CLIENT_LINE, size=10, color=GREY)
    p = doc.add_paragraph(); pfmt(p, 0, 2, WD_ALIGN_PARAGRAPH.CENTER)
    run(p, CONTRACT_LINE, size=10, color=GREY)
    p = doc.add_paragraph(); pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER)
    run(p, 'Archivo: ' + meta['code'] + '_V' + REV, size=9, color=GREY)
    # espaciador
    p = doc.add_paragraph(); pfmt(p, 60, 0)
    # tabla de revisiones
    rows = [['VERSIÓN', 'FECHA', 'DESCRIPCIÓN', 'ELABORÓ', 'REVISÓ', 'APROBÓ'],
            [REV, DATE, 'Creación inicial', '[Nombre]', '[Nombre]', '[Nombre]'],
            ['', '', '', 'Firma:', 'Firma:', 'Firma:']]
    t = doc.add_table(rows=3, cols=6)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t)
    set_table_widths(t, [800, 1250, 2350, 1650, 1650, 1660])
    for ri, r in enumerate(rows):
        row_no_split(t.rows[ri])
        for ci, txt in enumerate(r):
            c = t.cell(ri, ci); set_cell_margins(c, 70, 80, 70, 80)
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            p = c.paragraphs[0]; pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
            if ri == 0:
                set_cell_fill(c, NAVY); run(p, txt, size=8, bold=True, color='FFFFFF')
            else:
                run(p, txt, size=8, color=GREY if ri == 2 else TEXT)
    t.rows[2].height = Inches(0.45)
    p = doc.add_paragraph(); pfmt(p, 10, 0, WD_ALIGN_PARAGRAPH.CENTER)
    run(p, PROPERTY, size=7.5, color=GREY, italic=True)
    p.add_run().add_break(WD_BREAK.PAGE)

def build_toc(doc):
    p = doc.add_paragraph(); pfmt(p, 0, 8)
    run(p, 'ÍNDICE', size=12, bold=True, color=NAVY)
    p = doc.add_paragraph()
    add_field(p, 'TOC \\o "1-2" \\h \\z \\u')
    p = doc.add_paragraph(); p.add_run().add_break(WD_BREAK.PAGE)

# ---------------------------------------------------------------- parser markdown
def parse(md):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', md, re.S)
    if not m:
        raise ValueError('sin YAML')
    meta = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    return meta, md[m.end():]

def is_table_line(s):
    return s.strip().startswith('|') and s.strip().endswith('|') and len(s.strip()) > 1

def split_row(s):
    s = s.strip()[1:-1]
    return [c.strip() for c in s.split('|')]

def render_body(doc, body, numbering):
    lines = body.splitlines()
    i = 0; cur_dec = None; plain_next = False
    while i < len(lines):
        raw = lines[i]; s = raw.rstrip()
        st = s.strip()
        if not st:
            cur_dec = None; i += 1; continue
        if st == '{.plain}':
            plain_next = True; i += 1; continue
        if st == '\\pagebreak':
            p = doc.add_paragraph(); pfmt(p, 0, 0); p.add_run().add_break(WD_BREAK.PAGE)
            i += 1; continue
        hm = re.match(r'^(#{1,4})\s+(.*)$', st)
        if hm:
            lvl = len(hm.group(1))
            p = doc.add_paragraph(hm.group(2).replace('**', '').strip(), style=f'Heading {lvl}')
            cur_dec = None; i += 1; continue
        if is_table_line(st):
            rows = []
            while i < len(lines) and is_table_line(lines[i]):
                r = split_row(lines[i])
                if not all(re.match(r'^:?-{2,}:?$', c) for c in r if c) or not any(r):
                    rows.append(r)
                i += 1
            rows = [r for r in rows if not all(re.match(r'^:?-{2,}:?$', c) for c in r if c) or not any(c for c in r)]
            if rows:
                add_table(doc, rows, plain=plain_next)
            plain_next = False; cur_dec = None
            continue
        if st.startswith('>'):
            text = st.lstrip('>').strip()
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                text += ' ' + lines[i].strip().lstrip('>').strip(); i += 1
            add_callout(doc, text); cur_dec = None
            continue
        bm = re.match(r'^(\s*)[-*]\s+(.*)$', s)
        if bm:
            lvl = min(len(bm.group(1).replace('\t', '  ')) // 2, 2)
            p = doc.add_paragraph(); pfmt(p, 0, 2)
            if cur_dec is not None and lvl > 0:
                set_num(p, cur_dec, 1)
            else:
                set_num(p, numbering.bullet_id, lvl)
            add_inline(p, bm.group(2).strip())
            i += 1; continue
        nm = re.match(r'^(\s*)(\d+)[.)]\s+(.*)$', s)
        if nm:
            if cur_dec is None:
                cur_dec = numbering.new_decimal()
            p = doc.add_paragraph(); pfmt(p, 0, 3)
            set_num(p, cur_dec, 0)
            add_inline(p, nm.group(3).strip())
            i += 1; continue
        p = doc.add_paragraph(); pfmt(p, 0, 5)
        add_inline(p, st)
        cur_dec = None
        i += 1

def build(md_path, out_dir):
    md = open(md_path, encoding='utf-8').read()
    meta, body = parse(md)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.5); sec.page_height = Inches(11)
    sec.left_margin = sec.right_margin = Inches(1)
    sec.top_margin = Inches(1.45); sec.bottom_margin = Inches(0.95)
    sec.header_distance = Inches(0.4); sec.footer_distance = Inches(0.35)
    setup_styles(doc)
    numbering = Numbering(doc)
    sec.different_first_page_header_footer = True
    build_header(sec, meta)
    build_footer(sec.footer)
    fp = sec.first_page_footer; fp.is_linked_to_previous = False
    p = fp.paragraphs[0]; pfmt(p, 0, 0, WD_ALIGN_PARAGRAPH.CENTER, line=1.0)
    run(p, FOOTER_1, size=7, bold=True, color=NAVY)
    build_cover(doc, meta)
    build_toc(doc)
    render_body(doc, body, numbering)
    cp = doc.core_properties
    cp.title = meta['cover_title']; cp.subject = meta['code']; cp.author = AUTHOR
    cp.last_modified_by = AUTHOR; cp.comments = PROJECT + ' · ' + EMPRESA
    cp.keywords = 'Neptuno Energy Services; documento base; fotovoltaico; tracker; procedimiento'
    cp.language = 'es-CO'
    name = FILENAMES.get(meta['code'], meta['code'] + '_R00')
    out = os.path.join(out_dir, name + '.docx')
    doc.save(out)
    return out

if __name__ == '__main__':
    out_dir = os.path.join(HERE, 'out'); os.makedirs(out_dir, exist_ok=True)
    targets = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, 'content', '*.md')))
    for f in targets:
        try:
            print('OK ', build(f, out_dir))
        except Exception as e:
            import traceback; traceback.print_exc()
            print('ERR', f, e)
