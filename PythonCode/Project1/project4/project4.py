# project4.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

from sys import argv
from string import *
from index import *

bookname = argv[1]
book = open(bookname, "r")
ppfile = bookname.replace(".txt", "preprocessed.txt")
ppbook = open(ppfile, "w")
stopwords = list()
punc = punctuation
punc = punc.replace("--","")
punc = punc.replace("-","")
punc = punc.replace("'","")

for line in open("stopwords.txt", "r"):
    line = line.replace("\n", "")
    stopwords.append(line)

for line in book:
    line = line.lower()
    words = line.split()
    line = " ".join(i for i in words if i not in stopwords and len(i) >= 3)
    for c in punc:  # This is how to remove punctuation from a string
        # punctuation is an variable of the string module that contains a string
        # with all punctuation in it. It was modified to reflect not wanting
        # to remove hyphens and apostrophes.
        line = line.replace(c, "")
    words = line.split()
    line = " ".join(i for i in words if len(i) >= 3)
    line += "\n"
    ppbook.write(line)

ppbook.close()

index = Indexer(ppfile, bookname)

index.lookup()