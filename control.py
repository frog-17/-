import streamlit as st
from contents.main import main
from contents.login import login
from contents.register import register
from user import User

if 'next_page' not in st.session_state:
    st.session_state["user"] = User()
    st.session_state["next_page"] = "login"

def render_page():
    if st.session_state["next_page"] == "main":
        main()
    elif st.session_state["next_page"] == "login":
        login()
    elif st.session_state["next_page"] == "register":
        register()


if __name__ == "__main__":
    render_page()