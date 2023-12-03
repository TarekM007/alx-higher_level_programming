#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ""
    length = 0
    for char in sentence:
        length += 1
    if length == 0:
        return None
    else:
        first_char = sentence[0]
        return length, first_char
