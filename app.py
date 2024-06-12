from PIL import Image
from io import StringIO
import streamlit as st
from Modules.ai_improver import *
from Modules.constants import *
from Modules.cv_scanner import *

# ================================================================ #
# ================= Functions ==================================== #
# ================================================================ #


def profile_extractor(string_data):
    """Summary - Function takes string_data and extracts out the beginning 
        profile info.

    Args:
        string_data (String): The CV in string form

    Returns:
     String: The profile header portion of CV
    """
    cv_profile_section = string_data.split("SUMMARY:", maxsplit=1)[0]
    return cv_profile_section


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
        # Extract out the profile info
        profile_section = profile_extractor(string_data)

        st.subheader('Lets discuss the summary :male-detective:')
        # Submit the SUMMARY section to the OpenAI LLM for improvements
        reviewed_summary = summary_result(string_data)

        # Join profile_section & reviewed_summary
        updated_cv = profile_section + reviewed_summary

        # Let's process the experiences in the CV form
        st.subheader('Lets discuss the work experience :office:')
        experiences = experience_parser(string_data)
        st.write('We noticed that you added ' +
                 str(len(experience_parser(string_data))))

        # Iterate thru the experiences list
        for e in experiences:
            print('Experience:')
            # This prints splits e on [SEP} and prints the
            # second-to-last list item, which is the last line
            # of the experience because of the [SEP] on the last line
            # creates an empty extra list item. Then sends experience
            # to be updated by OpenAI. Lastly, it appends results to
            # the reviewed_experiences list.
            # print(e.split('[SEP]')[-2])
            review_experience = experience_result(e.split('[SEP]')[-2])
            reviewed_experiences.append(review_experience)

        # Write CV & EXPERIENCES to new_file(cv_improved.txt)
        for e in range(len(reviewed_experiences)):
            # Writes a line to new_file(i.e., "Experience 2")
            updated_cv += '\nEXPERIENCE:\n' + str(e + 1)

            start_text = "EXPERIENCE:" + str(e+1)
            end_text = "EXPERIENCE:" + str(e + 2)

            start_index = string_data.find(start_text)
            end_index = string_data.find(end_text)

            experience_text = string_data[start_index:end_index]
            print("review_experience item: \n", review_experience)
            input()

            updated_cv += experience_text + reviewed_experiences[e]
           

       # Write School history to CV
        schools = school_parser(string_data)
        updated_cv += schools

       # Write Contacts to CV
        contacts = contacts_parser(string_data)
        updated_cv += contacts

        new_file = open('cv_improved.txt', 'w+')
        new_file.write(updated_cv)

        new_file.close()
        download_result()
