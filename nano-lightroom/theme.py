"""Shared CSS for landing + app — dark, warm, premium feel."""
from __future__ import annotations

import streamlit as st

CSS = """
<style>
:root {
  --bg:        #0a0b10;
  --bg-soft:   #11141c;
  --bg-card:   #161a24;
  --border:    rgba(255,255,255,0.08);
  --text:      #f4f5f7;
  --text-soft: #9aa1ad;
  --accent:    #ffb74d;
  --accent-2:  #ff7ab3;
  --good:      #5fd897;
}

html, body, .stApp {
  background:
    radial-gradient(1100px 540px at 18% -8%, rgba(255,183,77,0.10), transparent 60%),
    radial-gradient(900px 450px at 110% 12%, rgba(255,122,179,0.09), transparent 70%),
    var(--bg) !important;
  color: var(--text);
  font-feature-settings: "ss01", "cv11";
}

/* ----- header bar ----- */
.nl-topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.6rem 0 1.2rem; border-bottom: 1px solid var(--border);
  margin-bottom: 1.5rem;
}
.nl-brand { display: flex; align-items: center; gap: 0.6rem; font-weight: 700; font-size: 1.05rem; }
.nl-brand .dot {
  width: 10px; height: 10px; border-radius: 999px;
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%);
  box-shadow: 0 0 14px rgba(255,184,77,0.55);
}
.nl-brand .name { letter-spacing: -0.01em; }
.nl-pill {
  font-size: 0.72rem; padding: 0.2rem 0.55rem; border-radius: 999px;
  background: rgba(255,183,77,0.12); color: var(--accent);
  border: 1px solid rgba(255,183,77,0.28);
}

/* ----- hero ----- */
.nl-hero { text-align: center; padding: 3rem 1rem 1.2rem; }
.nl-eyebrow {
  display: inline-block; font-size: 0.78rem; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--accent);
  background: rgba(255,183,77,0.10); border: 1px solid rgba(255,183,77,0.22);
  padding: 0.32rem 0.7rem; border-radius: 999px; margin-bottom: 1.4rem;
}
.nl-hero h1 {
  font-size: clamp(2.4rem, 6vw, 3.8rem);
  font-weight: 800; line-height: 1.04; letter-spacing: -0.035em;
  background: linear-gradient(135deg, #fff 0%, #ffe1b3 50%, #ffb3d6 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  margin: 0 0 1rem;
}
.nl-hero p.sub {
  font-size: clamp(1rem, 1.6vw, 1.18rem);
  color: var(--text-soft); max-width: 620px; margin: 0 auto 1.4rem;
  line-height: 1.55;
}

/* ----- features grid ----- */
.nl-feature {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 14px; padding: 1.4rem 1.3rem; height: 100%;
}
.nl-feature .icon {
  font-size: 1.4rem; margin-bottom: 0.6rem; display: block;
}
.nl-feature h3 {
  font-size: 1rem; margin: 0 0 0.4rem; color: var(--text); font-weight: 600;
}
.nl-feature p {
  font-size: 0.88rem; color: var(--text-soft); margin: 0; line-height: 1.5;
}

/* ----- login card ----- */
.nl-login-wrap { display: flex; justify-content: center; padding: 1.5rem 0 3rem; }
.nl-login-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 1.8rem 1.6rem 1.4rem;
  width: 100%; max-width: 380px;
  box-shadow: 0 20px 60px -20px rgba(0,0,0,0.5);
}
.nl-login-card h3 { margin: 0 0 0.3rem; font-size: 1.1rem; }
.nl-login-card .muted { color: var(--text-soft); font-size: 0.85rem; margin: 0 0 1rem; }

/* ----- pricing teaser ----- */
.nl-pricing { padding: 2rem 0 1rem; }
.nl-tier {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 14px; padding: 1.4rem; height: 100%;
}
.nl-tier.featured {
  border-color: rgba(255,183,77,0.5);
  box-shadow: 0 0 0 1px rgba(255,183,77,0.18), 0 20px 60px -25px rgba(255,183,77,0.18);
}
.nl-tier h4 { margin: 0 0 0.2rem; font-size: 1rem; }
.nl-tier .price { font-size: 1.6rem; font-weight: 700; margin: 0.3rem 0 0.8rem; }
.nl-tier .price .small { font-size: 0.8rem; font-weight: 400; color: var(--text-soft); }
.nl-tier ul { list-style: none; padding: 0; margin: 0.6rem 0 0; }
.nl-tier li { font-size: 0.86rem; color: var(--text-soft); padding: 0.22rem 0; }
.nl-tier li::before { content: "✓ "; color: var(--good); font-weight: 700; }

/* ----- footer ----- */
.nl-foot {
  text-align: center; color: var(--text-soft); font-size: 0.78rem;
  padding: 2rem 0 0.5rem; border-top: 1px solid var(--border); margin-top: 2rem;
}

/* ----- streamlit overrides ----- */
button[kind="primary"] {
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%) !important;
  border: none !important; color: #1a1208 !important; font-weight: 600 !important;
}
button[kind="primary"]:hover { filter: brightness(1.08); }

div[data-testid="stFileUploader"] section {
  background: var(--bg-soft); border: 1px dashed var(--border) !important;
  border-radius: 12px;
}

/* hide default streamlit chrome on landing for a cleaner look */
.nl-clean header[data-testid="stHeader"] { background: transparent; }
</style>
"""


def inject() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def topbar(authenticated: bool, on_signout=None) -> None:
    """Render brand bar. When authenticated, includes a sign-out button."""
    cols = st.columns([6, 2])
    with cols[0]:
        st.markdown(
            '<div class="nl-brand">'
            '<span class="dot"></span>'
            '<span class="name">Nano Lightroom</span>'
            '<span class="nl-pill">beta</span>'
            "</div>",
            unsafe_allow_html=True,
        )
    with cols[1]:
        if authenticated and on_signout:
            if st.button("Sign out", use_container_width=True, key="nl_signout_btn"):
                on_signout()
    st.markdown('<div style="height:8px;border-bottom:1px solid var(--border);margin-bottom:1.2rem"></div>', unsafe_allow_html=True)
