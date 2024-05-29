import streamlit as st
from constants import *


def download_template(template_file=TEMPLATE_FILE):
    content_file = open(template_file, 'r')
    content = content_file.read()
    # Defaults to 'text/plain')
    st.download_button(
        'The first step is to fill the CV. Download the template here :rocket:', content)
    content_file.close()


def download_result(template_file=RESULT_FILE):
    content_file = open(template_file, 'r')
    content = content_file.read()
    # Defaults to 'text/plain'
    st.download_button(
        'Download the result of your AI improved CV here :wink:', content)
    content_file.close()
