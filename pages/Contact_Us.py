import streamlit as st
import pandas as pd
from send_email import send_email

df_topics = pd.read_csv('topics.csv')

with st.form(key='send_email'):
    user_email = st.text_input("Your email address")
    topic = st.selectbox('Topic', df_topics['topic'])
    msg = st.text_area("Your message")
    button = st.form_submit_button("Submit")

message = f"""\
Subject: {topic} from {user_email}

{msg}\n\nFrom: {user_email}
"""

if button:
    send_email(message)
    st.info("Request sent successfully!")
