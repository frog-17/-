import streamlit as st

def main():
    st.write("main")
    
    if st.button(label="ログイン", key="login_btn"):
        st.session_state["next_page"] = "login" 
        st.rerun()
    
    if st.button(label="新規登録", key="register_btn"):
        st.session_state["next_page"] = "register"
        st.rerun()
        
        
    