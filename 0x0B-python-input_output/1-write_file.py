#!/usr/bin/python3
"""number_of_lines
"""

def write_file(filename="", text=""):
    """
        Takes str filename to read, and str text to write
    """

    with open(filename, 'w', encoding='utf-8') as writeFile:
    wf = writeFile.write(text)
    return len(text)
