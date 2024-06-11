import streamlit as st
import re
from Modules.constants import *


def download_template(template_file=TEMPLATE_FILE):
    """Summary - Function opens the template_file(cv_template.txt) for reading
    and puts contents into variable "content".

    Args:
        template_file (file, optional): The CV template file. Defaults to TEMPLATE_FILE.
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
                creating a list(list_experiences), attempts to convert the first character of 
                each experience to an integer, and adds the experience to the `selected_experience`
                list if the conversion is successful.  

        Args:
        text_cv (String): The CV form text.

        Returns:
        List: Containing experiences from the CV.
    """
    list_experiences = text_cv.split('EXPERIENCE ')

    selected_experience = []
    for l in list_experiences:
        try:
            # This is a check that first character of l is
            # an integer, because original form began each
            # experience with a number.
            int(l[0][0])
            selected_experience.append(l)

        except:
            continue

    return selected_experience


def school_parser(text_cv):
    """Summary - Function takes the CV text and splits the string on the text "SCHOOL"
                creating a list(school_history), attempts to convert the first character of 
                each school to an integer, and adds the school to the `selected_school`
                list if the conversion is successful.  

        Args:
        text_cv (String): The CV form text.

        Returns:
        List: Containing schools from the CV.
    """
    # school_history = text_cv.split('SCHOOL ')
    school_history = re.split('SCHOOL ', text_cv)

    selected_school = []
    # Loop thru
    for item in school_history:
        try:
            # This is a check that first character of item is
            # an integer.
            int(item[0][0])
            selected_school.append(item)

        except:
            continue

    return selected_school
