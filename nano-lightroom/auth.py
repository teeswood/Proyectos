"""Password gate. Bcrypt hash lives in env or Streamlit secrets — never in code."""
from __future__ import annotations

import os

import bcrypt
import streamlit as st

_SESSION_KEY = "nl_authenticated"


def _get_user_hash() -> str | None:
    h = os.getenv("LR_USER_HASH")
    if h:
        return h
    try:
        return st.secrets["LR_USER_HASH"]
    except Exception:
        return None


def is_authenticated() -> bool:
    return bool(st.session_state.get(_SESSION_KEY, False))


def sign_out() -> None:
    st.session_state[_SESSION_KEY] = False
    st.rerun()


def login_form() -> None:
    """Render the login form. Sets session state and reruns on success."""
    user_hash = _get_user_hash()
    if not user_hash:
        st.error(
            "Auth not configured yet. Add `LR_USER_HASH` (bcrypt hash) to "
            "Streamlit Cloud → Settings → Secrets, then reload."
        )
        st.stop()

    with st.form("nl_login", clear_on_submit=False):
        pwd = st.text_input(
            "Password",
            type="password",
            placeholder="••••••••",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button(
            "Sign in", type="primary", use_container_width=True
        )

    if submitted:
        if not pwd:
            st.warning("Enter your password.")
        elif bcrypt.checkpw(pwd.encode("utf-8"), user_hash.encode("utf-8")):
            st.session_state[_SESSION_KEY] = True
            st.rerun()
        else:
            st.error("Wrong password.")
