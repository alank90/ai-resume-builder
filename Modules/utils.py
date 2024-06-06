from Modules.constants import *


def get_fixedkey_text(key, text):
    """ Summary - Function gets passed a key value from the FIXED_KEYS
        list and a copy of the CV form.

    Args:
        key (String): item in the list ORDERED_KEYS or FIXED_KEYS
        text (file(string)): CV form filled out by user

    Returns:
        String: The CV portion from the beginning to end of the section
         represented by the value in the "key" parameter. ie. SUMMARY or EXPERIENCE
    """
    # finds the index of the `key` parameter in the list `ORDERED_KEYS`
    # and assigns it to the variable `key_order`
    key_order = ORDERED_KEYS.index(key)
    # Get next item in list(ORDERED_KEYS) after key item
    next_key = ORDERED_KEYS[key_order+1]
    # splits the `text` parameter based on the `key` followed by a colon `':'`.
    # It takes the second part of the split (index 1) which should be the text
    # after the key and colon, and assigns it to the variable `start_text`
    start_text = text.split(key+':')[1]
    # finds the index of the `next_key`
    # within the `start_text`
    find_stop = start_text.find(next_key)
    # creates a substring of `start_text` starting from index 0 up to
    # (but not including) the index of `find_stop` string value
    trimmed_text = start_text[0:find_stop]
    # Strip out new line characters
    trimmed_text = trimmed_text.replace('\n', '')

    return trimmed_text


def extract_content(name_of_file):
    """Summary - Open CV file and read contents into variable
        content.

    Args:
        name_of_file (String): CV file name.

    Returns:
        String: CV's contents
    """
    file = open(name_of_file, 'r')
    content = file.read()
    file.close()
    return content
