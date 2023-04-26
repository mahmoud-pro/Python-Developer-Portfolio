import streamlit as st
from Send_Email import send_email

st.set_page_config(page_title="Mahmoud Taha | Portfolio", page_icon="assets/images/web_icon.ico",
                   layout="centered", initial_sidebar_state="auto", menu_items=None)
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address", key="email")
    # user_pass = st.text_input("Your password", key="password", type="password")
    email_subject = st.text_input("Your email subject")
    raw_message = st.text_area("Your message")

    message = f"Subject: {email_subject} \n\n {raw_message} \n {user_email}"
    submitted = st.form_submit_button("Submit")
    if submitted:
        send_email(message)
        st.info("Your email was sent successfully.", icon="🚀")