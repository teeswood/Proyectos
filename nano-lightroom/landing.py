"""Pre-auth landing page: hero, features, pricing, sign-in card."""
from __future__ import annotations

import streamlit as st

from auth import login_form
from theme import inject, topbar


_FEATURES = [
    ("⚡", "Batch real",
     "Subí 100 fotos. Una pasada. ZIP listo para descargar."),
    ("🎨", "10 looks cinematográficos",
     "Cinematic, Portra 400, B&N editorial, Golden Hour, Nordic, Faded Matte…"),
    ("🛡️", "Identidad intacta",
     "Solo color, contraste y luz. Rostros, gestos y composición no se tocan."),
    ("🧪", "Motor local + IA",
     "Pixel-true gratis con Pillow/numpy. IA opcional con Nano Banana para looks generativos."),
    ("📱", "Sin instalación",
     "Funciona desde el iPhone. Subí, procesá, descargá. No hay app que actualizar."),
    ("🔒", "Privado por defecto",
     "Las fotos se procesan en sesión. No se guardan. Acceso bajo password."),
]


def render() -> None:
    inject()
    topbar(authenticated=False)

    st.markdown(
        """
        <div class="nl-hero">
          <span class="nl-eyebrow">Color grading batch · web · iPhone</span>
          <h1>Editá 100 fotos<br/>en menos de un minuto</h1>
          <p class="sub">
            Lightroom-style presets aplicados en bloque. Motor local pixel-true gratis,
            o IA opcional para looks generativos. Caras y composición jamás se alteran.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    rows = [_FEATURES[:3], _FEATURES[3:]]
    for row in rows:
        cols = st.columns(3, gap="medium")
        for col, (icon, title, body) in zip(cols, row):
            with col:
                st.markdown(
                    f'<div class="nl-feature">'
                    f'<span class="icon">{icon}</span>'
                    f'<h3>{title}</h3>'
                    f'<p>{body}</p>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

    st.markdown('<div class="nl-login-wrap">', unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(
            '<div class="nl-login-card">'
            '<h3>Acceso</h3>'
            '<p class="muted">Privado. Pedile la contraseña al admin.</p>'
            '</div>',
            unsafe_allow_html=True,
        )
        login_form()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="nl-pricing">'
        '<h2 style="text-align:center;font-size:1.4rem;margin:0 0 1.2rem">Planes (en evaluación)</h2>'
        '</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(3, gap="medium")
    tiers = [
        ("Free", "$0", "siempre",
         ["Motor local pixel-true", "10 presets", "Batch hasta 20 fotos", "JPEG / PNG / WebP"], False),
        ("Pro", "$9", "/ mes",
         ["Todo lo del Free", "Motor IA (Nano Banana)", "Batch ilimitado", "Presets exclusivos", "Sin marca de agua"], True),
        ("Studio", "$29", "/ mes",
         ["Todo lo del Pro", "Acceso multiusuario", "API privada", "Soporte prioritario"], False),
    ]
    for col, (name, price, unit, items, featured) in zip(cols, tiers):
        with col:
            cls = "nl-tier featured" if featured else "nl-tier"
            li = "".join(f"<li>{i}</li>" for i in items)
            st.markdown(
                f'<div class="{cls}">'
                f'<h4>{name}</h4>'
                f'<p class="price">{price} <span class="small">{unit}</span></p>'
                f'<ul>{li}</ul>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        '<div class="nl-foot">© 2026 Nano Lightroom · '
        'Built on Streamlit · Identity-locked grading</div>',
        unsafe_allow_html=True,
    )
