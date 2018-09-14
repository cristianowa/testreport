
import os
from sections import *

def Report2Md(sequence, directory, separator=";"):
    title = filter(lambda x: x[0] == TITLE, sequence)
    if len(title) != 1:
        raise Exception("Test case must provide a single title")
    title = title[0][1]
    entries = filter(lambda x: x[0] != TITLE, sequence)
    filename = os.path.join(directory, title + ".md")
    with open(filename, "w") as fp:
        fp.write("# ")
        fp.write(title)
        fp.write("\n")
        for entry in entries:
            if entry[0] == EXPLANATION:
                fp.write(entry[1])
                fp.write("\n")
            elif entry[0] == TIP:
                fp.write(">")
                fp.write(entry[1].replace("\n", "\n>"))
                fp.write("\n")
            elif entry[0] == CODE:
                fp.write("```\n")
                fp.write(entry[1])
                fp.write("\n```\n")
            else:
                raise Exception("Invalid entry!")


if __name__ == '__main__':
    import tempfile
    tmp = tempfile.mktemp()
    print tmp
    Report2Md([
        (TITLE, "title"),
        (EXPLANATION, "explanation"),
        (CODE, """<html>
        <title> </title>
        <body> </body>
        </html>"""),
        (TIP, "a tip"),

    ], tmp)