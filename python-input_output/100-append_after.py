#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename) as f:
        lines = f.readlines()
    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)
    with open(filename, "w") as f:
        f.writelines(result)
