#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after ., ? and : 
    characters
"""


def text_indentation(text):
    """
    takes one argument - text
    prints 2 new lines after ., ? and : found in text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    wild = ['.', '?', ':']
    new_text = ""
    for letter in text:
        new_text += letter
        if letter in wild:
            new_text += "\n"
            print(new_text.strip(" "))
            new_text = ""
    if letter not in wild:
        print(new_text.strip(" "), end="")
