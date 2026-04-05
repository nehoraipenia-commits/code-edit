import streamlit as st
from streamlit_ace import st_ace
import sys
from io import StringIO

st.set_page_config(page_title="StreamCode", layout="wide")

st.title("💻 StreamCode Editor")

# Configuration dans la barre latérale
st.sidebar.title("Configuration")
# Utilise "c_cpp" au lieu de "cpp" pour éviter l'erreur de ton terminal
langage = st.sidebar.selectbox("Langage", ["python", "c_cpp", "javascript", "html", "markdown"])
theme = st.sidebar.selectbox("Thème", ["monokai", "github", "dracula"])

# L'éditeur
contenu = st_ace(
    language=langage,
    theme=theme,
    height=400,
    font_size=14,
    key="editor"
)

# Fonctionnalité bonus : Exécuter le code Python
if langage == "python" and contenu:
    if st.button("▶️ Exécuter le code Python"):
        st.subheader("Console Output :")
        # Redirection de la sortie standard pour capturer les print()
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        
        try:
            exec(contenu)
            st.code(redirected_output.getvalue())
        except Exception as e:
            st.error(f"Erreur : {e}")
        finally:
            sys.stdout = old_stdout

if contenu:
    # Créer un nom de fichier dynamique selon le langage
    extension = "py" if langage == "python" else "cpp" if langage == "c_cpp" else "txt"
    
    st.download_button(
        label="💾 Enregistrer le fichier",
        data=contenu,
        file_name=f"mon_code.{extension}",
        mime="text/plain",
    )