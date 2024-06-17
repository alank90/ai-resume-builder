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


def ai_experience_improver(experiences_list):
    """ Summary - Function sends CV experience section to OPENAI to generate
         AI generated section.

    Args:
        experiences_list (List): List of the stripped out last line EXPERIENNCE
        description of the experiences sections.

    Returns:
        List: OPENAI generated improved experience description list.
    """
    st.write('Improving the work experience for you!')

    # Iterate thru the experiences_list list
    for index, item in enumerate(experiences_list):
        # This loop splits experiences_list list item on [SEP] and sends the last line of
        # the experience section to OpenAI to improve it. It then
        # appends improved description to list reviewed_experiences. Now have a
        # list of improved experience descriptions. Still need to merge each
        # experiences_list list item first three lines with improved experience
        # description.

        # Improve the EXPERIENCE description
        original_experience_description = item.split('[SEP]')

        ai_experince_description_improved = ai_single_experience_improver(
            original_experience_description[-2])

        # Update EXPERIENCE section with ai improved description
        experiences_list[index] = experiences_list[index].replace(
            original_experience_description[-2], ai_experince_description_improved)

    return experiences_list

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
    ai_improved_experiences_list = []

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

        # Let's process the experiences_list in the CV form and improve
        # the descriptions in each EXPERIENCE section.
        st.subheader('Lets discuss the work experience :office:')
        experiences_list = experience_parser(string_data)
        st.write('We noticed that you added ' +
                 str(len(experience_parser(string_data))) + ' work experiences_list')

        ai_updated_experiences_list = ai_experience_improver(experiences_list)

        # Construct new improved Experiences section
        for e in range(len(ai_updated_experiences_list)):
            print("The updated experience description: \n",
                  ai_updated_experiences_list[e], e)
            # Updates the file
            updated_cv = updated_cv + '\nEXPERIENCE: \n' + str(e + 1)
            updated_cv = updated_cv + ai_updated_experiences_list[e]

       # Write School history to CV
        """ schools_text = school_parser(string_data)

        updated_cv = updated_cv + schools_text """

       # Write Contacts to CV
        """ contacts = contacts_parser(string_data)
        updated_cv = updated_cv + contacts """

        new_file = open('cv_improved.txt', 'w+')
        new_file.write(updated_cv)

        new_file.close()
        download_result()
