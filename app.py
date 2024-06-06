from PIL import Image
from io import StringIO
import streamlit as st
from Modules.ai_improver import *
from Modules.constants import *
from Modules.cv_scanner import *

# ================================================================ #
# ================= Functions ==================================== #
# ================================================================ #


def summary_result(string_data):
    """ Summary - Function takes CV form and runs it thru OpenAI 
         Completion method to improve the CV summary portion.

    Args:
        string_data (string): Original CV form

    Returns:
        String: Updated OpenAI generated CV SUMMARY text section. 
    """
    st.write('Improving the summary for you! :rocket:')

    # This will return a portion of the CV up to end of the SUMMARY
    # section.
    trimmed_text = get_fixedkey_text(FIXED_KEYS[1], string_data)
    text = summary_corrector(trimmed_text)

    return text


def experience_result(experience_text):
    """ Summary - Function sends CV experience section to OPENAI to generate  
         AI generated section.

    Args:
        experience_text (String): Original experience section text

    Returns:
        String: OPENAI generated text
    """
    st.write('Improving the work experience for you!')
    text = single_experience_corrector(experience_text)

    return text

# ------------------------------------------------------------------------------------------- #


# ================================================================ #
# ================= Main Procedure =============================== #
# ================================================================ #
if __name__ == '__main__':
    image = Image.open('images/resume_image.jpeg')
    st.image(image, caption='Photo by Unseen Studio on Unsplash')
    st.header('Improving your CV in seconds using ChatGPT!')
    st.write('This app is meant to improve the quality of your CV by using Artificial Intelligence\n Start by downloading the template, fill the information, upload your CV and enjoy the magic! :smile:')
    st.write("\n Let's see what you got! Download the following template and fill it out with your information! :sunglasses:")
    download_template()
    uploaded_file = st.file_uploader("Upload your CV here! :point_down")
    reviewed_experiences = []

    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
        # Read filled out form into string_data
        string_data = stringio.read()

        st.subheader('Lets discuss the summary :male-detective:')
        # Submit the SUMMARY section to the OpenAI LLM for improvements
        reviewed_summary = summary_result(string_data)

        # Let's process the experiences in the CV form
        st.subheader('Lets discuss the work experience :office:')
        experiences = experience_parser(string_data)
        print("This is the parsed original experiences:", experiences)
        st.write('We noticed that you added ' +
                 str(len(experience_parser(string_data))))

        # Iterate thru the experiences list
        for e in experiences:
            print('Experience:')
            # This prints experiences rom the second-to-last
            print(e.split('[SEP]')[-2])

        # Write SUMMARY and EXPERIENCES to cv_improved.txt
        new_file = open('cv_improved.txt', 'w+')
        new_file.write('SUMMARY:\n')
        new_file.write(reviewed_summary)

        for e in range(len(reviewed_experiences)):
            new_file.write('\nEXPERIENCE %i \n' % (e))
            new_file.write(reviewed_experiences[e])

        new_file.close()
        download_result()
