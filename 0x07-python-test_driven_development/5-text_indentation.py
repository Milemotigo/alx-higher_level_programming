#!/usr/bin/python3

def text_indentation(text):
    # check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # replace every occurance of  [. ? :] characters with the exqct characters

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    # remove an extra newline that may have been added at the end
    text = text.rstrip()

    print(text)

