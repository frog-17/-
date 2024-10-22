import streamlit as st 

def login():
    submit_btn = False
    with st.form(key="login"):
        login_html = """
        <style>
            .center {
                text-align: center;
            }
        </style>
        <h1 class='center'>ログイン</h1>
        """
        st.markdown(login_html, unsafe_allow_html=True)
        space_30_html = """
        <style>
            .space_30 {
                padding: 30px 0px;
            }
        </style>
        <div class='space_30'></div>
        """
        space_60_html = """
        <style>
            .space_60 {
                padding: 60px 0px;
            }
        </style>
        <div class='space_60'></div>
        """
        st.markdown(space_30_html, unsafe_allow_html=True)
        
        message = st.text("")
        user_id = st.text_input("ID", key="user_id")
        password = st.text_input("パスワード", type="password", key="password")

        st.markdown(space_60_html, unsafe_allow_html=True)
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            pass
        with col_2:
            submit_btn = st.form_submit_button("ログイン", use_container_width=True)
        with col_3:
            pass
    
    if submit_btn == True:
        if user_id == "" or user_id == None:
            message.error("IDを入力してください")
        elif password == "" or password == None:
            message.error("パスワードを入力してください")
        else:
            st.session_state["next_page"] = "main"
            st.rerun()