import streamlit as st 

def register():
    submit_btn = False
    with st.form(key="register"):
        register_html = """
        <style>
            .center {
                text-align: center;
            }
        </style>
        <h1 class='center'>新規登録</h1>
        """
        st.markdown(register_html, unsafe_allow_html=True)
        space_html = """
        <style>
            .space {
                padding: 20px 0px;
            }
        </style>
        <div class='space'></div>
        """
        st.markdown(space_html, unsafe_allow_html=True)

        message = st.text("")
        user_id = st.text_input("ID", key="user_id")
        mail_address = st.text_input("メールアドレス", key="mail_address")
        password = st.text_input("パスワード", type="password", key="password")
        nick_name = st.text_input("ニックネーム", key="nick_name")

        st.markdown(space_html, unsafe_allow_html=True)

        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            pass
        with col_2:
            submit_btn = st.form_submit_button("登録", use_container_width=True)
        with col_3:
            pass
    
    if submit_btn == True:
        if user_id == "" or user_id == None:
            message.error("IDを入力してください")
        elif mail_address == "":
            message.error("メールアドレスを入力してください")
        elif password == "":
            message.error("パスワードを入力してください")
        elif nick_name == "":
            message.error("ニックネームを入力してください")
        else:
            st.session_state["next_page"] = "main"
            st.rerun()