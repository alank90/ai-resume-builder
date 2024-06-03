import streamlit as st
import openai
from utils import *
from constants import *
openai.api_key = OPENAIKEY


def general_corrector(prompt, temperature, model=OPENAIMODEL, max_tokens=20):
    """ Summary - Function uses the OpenAI Completion module. You give it
      a prompt and it returns a text completion, generated according to your
      parameters. 

    Args:
        prompt (String): A section from user's CV
        temperature (int): OpenAI parameter
        model String, optional): The LLM used(ie., GPT-Turbo-3.5). Defaults to OPENAIMODEL.
        max_tokens (int, optional): Maximum size of response. Defaults to 20.

    Returns:
        String: OpenAi's Completions API response's text field property to the
          request.
    """
    openai.api_key = OPENAIKEY
    res = openai.Completion.create(
        model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    return res['choices'][0]['text']


def single_experience_corrector(experience_text):
    """Summary - Function calls the general_contractor() function with 
        prompt constructed from EXPERIENCE_PROMPT_CONVERT constant & other parameters
    Args:
        experience_text (String): Text rom the Expeience section of the CV

    Returns:
        String: Updated Experience section returned by OpenAI.
    """
    correct_text = general_corrector(
        prompt=EXPERIENCE_PROMPT_CONVERT+experience_text, temperature=0.4, max_tokens=200)

    st.markdown("<span style='color:lightblue'>" +
                experience_text+"</span>", unsafe_allow_html=True)
    st.text('The AI suggests the following summary instead: \n')
    # print(final_correction)
    st.markdown("<span style='color:red'>"+correct_text +
                "</span>", unsafe_allow_html=True)

    return correct_text


def summary_corrector(summary_text):
    """Summary - The function calls general_corrector() twice to improve the Summary
      section of the CV. It then outputs the section using Stramlit.

    Args:
        summary_text (String): Original summary text in the CV.

    Returns:
        String: Improved Summary section from OpenAI model.
    """
    print('The AI is rephrasing the text (if necessary): \n')
    st.text('The AI is rephrasing the text (if necessary): \n')
    first_correction = general_corrector(
        prompt=SUMMARY_PROMPT_CONVERT+summary_text, temperature=TEMPERATURE_SUMMARY_PROMPT_CONVERT, max_tokens=200)
    print('The AI is improving the rephrased summary \n')
    st.text('The AI is improving the rephrased summary \n')
    final_correction = general_corrector(
        prompt=SUMMARY_PROMPT_IMPROVER+first_correction, temperature=TEMPERATURE_SUMMARY_PROMPT_IMPROVER, max_tokens=200)
    print('The summary of your current CV is the following: \n')
    st.text('The AI is improving the rephrased summary \n')
    print(summary_text)
    # st.text (summary_text)
    st.text('The summary section of your CV is the following one: \n')
    st.markdown("<span style='color:lightblue'>" +
                summary_text+"</span>", unsafe_allow_html=True)
    st.text('The AI suggests the following summary instead: \n')
    print(final_correction)
    st.markdown("<span style='color:red'>"+final_correction +
                "</span>", unsafe_allow_html=True)

    return final_correction


def summary_corrector_main(summary_text):
    """Summary - Function used to improve the Summary section of the CV when using
        main.py script.

    Args:
        summary_text (String): Summary text from the CV.

    Returns:
        String: Improved Summary text section using OpenAI model.
    """
    first_correction = general_corrector(
        prompt=SUMMARY_PROMPT_CONVERT+summary_text, temperature=TEMPERATURE_SUMMARY_PROMPT_CONVERT, max_tokens=200)
    final_correction = general_corrector(
        prompt=SUMMARY_PROMPT_IMPROVER+first_correction, temperature=TEMPERATURE_SUMMARY_PROMPT_IMPROVER, max_tokens=200)

    return final_correction


def single_experience_corrector_main(experience_text):
    """Summary - Function used to improve the Experience section of the CV when using
        main.py script.

    Args:
        experience_text (String):The original Experience section of CV.

    Returns:
       String: The updated Experience section from OpenAI model.
    """
    correct_text = general_corrector(
        prompt=EXPERIENCE_PROMPT_CONVERT+experience_text, temperature=0.4, max_tokens=200)

    return correct_text
