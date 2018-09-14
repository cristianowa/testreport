import os
from sections import *


def Report2Csv(sequence, directory, separator=";"):
    title = filter(lambda x:x[0] == TITLE, sequence)
    if len(title) != 1:
        raise Exception("Test case must provide a single title")
    title = title[0][1]
    entries = filter(lambda x:x[0] != TITLE, sequence)
    filename = os.path.join(directory, title + ".csv")
    with open(filename, "w") as fp:
        fp.write(title)
        fp.write("\n")
        for entry in entries:
            fp.write(separator.join(list(entry)))
            fp.write("\n")



if __name__ == '__main__':
    import tempfile
    tmp = tempfile.mktemp()
    print tmp
    Report2Csv([
        (TITLE, "title"),
        (CODE, "code"),
        (TIP, "a tip"),

    ], tmp)