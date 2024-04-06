#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i == n:
            new_str = str.replace(str[i], "")
            return new_str
        elif n > len(str) or n < 0:
            return str
