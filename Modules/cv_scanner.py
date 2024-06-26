import streamlit as st
from Modules.constants import *

# =================================================================================== #
# ========================= Function Modules ======================================== #
# =================================================================================== #


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

# -------------------------------------------------------------------------------------------- #


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

# -------------------------------------------------------------------------------------------- #


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
            # an integer, because each list item should begin
            # with an integer
            int(l[0][0])
            selected_experience.append(l)

        except:
            continue

    return selected_experience

# -------------------------------------------------------------------------------------------- #


def school_parser(text_cv):
    """Summary - Function takes the CV text and splits the string on the text "SCHOOL 1:"
                  and "CONTACTS" returning the Schools section of the CV.
        Args:
        text_cv (String): The CV form text.

        Returns:
        The txt_cv SCHOOLS subsection.
    """
    start_text = "SCHOOL 1:"
    end_text = "CONTACTS:"

    start_index = text_cv.find(start_text)
    end_index = text_cv.find(end_text)

    school_subsection = text_cv[start_index:end_index]

    return school_subsection

# -------------------------------------------------------------------------------------------- #


def contacts_parser(text_cv):
    """Summary - Function takes the CV text and splits the string on the text "CONTACTS:"
                creating a substring of the CONTACTS section of the cv.

        Args:
        text_cv (String): The CV form text.

        Returns:
        String: CONTACTS section of the CV.
    """
    start_text = "CONTACTS:"
    start_index = text_cv.find(start_text)
    contacts = text_cv[start_index:]

    return contacts
