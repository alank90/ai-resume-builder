import streamlit as st
from constants import *


def download_template(template_file=TEMPLATE_FILE):
    """Summary - Function opens the template_file(cv_example.txt) for reading
    and reads its contents and puts file contents into variable "content".

    Args:
        template_file (file, optional): The CV file. Defaults to TEMPLATE_FILE.
    """
    content_file = open(template_file, 'r')
    content = content_file.read()
    # Defaults to 'text/plain')
    st.download_button(
        'The first step is to fill the CV. Download the template here :rocket:', content)
    content_file.close()


def download_result(template_file=RESULT_FILE):
    """Summary - Function reads the contents of the template file and also creates a 
        download button using Streamlit for user to download the updated CV.

    Args:
        template_file (
            , optional): By default, the cv_example.txt file. Defaults to RESULT_FILE.
    """
    content_file = open(template_file, 'r')
    content = content_file.read()
    # Defaults to 'text/plain'
    st.download_button(
        'Download the result of your AI improved CV here :wink:', content)
    content_file.close()


def experience_parser(text_cv):
    """Summary - Function takes the CV text and splits the string on the text "EXPERIENCE"
    creating a list(list_experiences),attempts to convert the first character of 
    the first element of each experience to an integer, and adds the experience 
    to the `selected_experience` list if the conversion is successful.  

    Args:
    text_cv (String): This is the text read into the string_data variable
    from the StringIO operation from app.py.

    Returns:
        List: Containing experiences from the CV.
    """
    list_experiences = text_cv.split('EXPERIENCE')
    selected_experience = []
    for l in list_experiences:
        try:
            int(l[0][0])
            selected_experience.append(l)
        except:
            continue

    return selected_experience
