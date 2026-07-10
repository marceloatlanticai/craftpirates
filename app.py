import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="feita de pontos — sala de criação",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# esconde o chrome do Streamlit e remove os espaçamentos
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

# injeta a chave do Gemini a partir dos secrets do Streamlit
# (em .streamlit/secrets.toml localmente, ou em Settings → Secrets no Streamlit Cloud)
try:
    gemini_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    gemini_key = ""
html = html.replace("__GEMINI_KEY__", gemini_key)

components.html(html, height=920, scrolling=False)
