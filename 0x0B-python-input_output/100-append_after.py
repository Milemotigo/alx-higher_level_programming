#!/usr/bin/python3
'''search and update'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()

    for i in range(lines):
        if search_string in lines[i]:
            lines.insert += new_string
        if not search_string in lines[i]:
            lines.append += newstring
    f.seek(0)
    f.writeline(lines)
