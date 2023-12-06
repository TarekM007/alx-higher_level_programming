#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    mod_names = [name for name in dir(hidden_4) if not name.startswith('__')]
    for name in mod_names:
        print(name)
