# index.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

from avl_tree import *
from string import *


class Indexer():
    """Class that will handle all the indexing of the preprocessed file"""

    def __init__(self, preproccessed, original):
        self.preprocessed = open(preproccessed, 'r')
        self.indextree = AVLTreeMap()
        self.original = original
        linenum = 1
        
        for line in self.preprocessed:
            words = line.split()  # Splits the line into words to be placed
            # into the AVL Tree
            for i in words:
                if i not in self.indextree:  # Only makes another key if it
                # is not in the tree already
                    self.indextree[i] = list()
                    self.indextree[i] += [linenum]
                else:
                    if linenum not in self.indextree[i]:
                        self.indextree[i] += [linenum]
            linenum += 1  # Used to manually count the line numbers to add to
            #  the list

    def lookup(self):
        word = None
        book = open(self.original, "r")
        while word != ("y" or "Y"):  # Only stops once the user asks wants to
        #  dump the index to a file
            word = input("What word are you looking for?\n").lower()
            print("------------------------------------------------------")
            if word == '':
                word = input("Would you like to dump the index? Y/N\n")
                print("------------------------------------------------------")
            elif word in self.indextree:
                i = 1
                for line in book:  # If it is in the tree it prints the lines
                #  of the book that it appears on.
                    if i in self.indextree[word]:
                        print(line)
                    i += 1
                print("------------------------------------------------------")
            else:
                print("The word you are looking for was not found.\n")
                print("------------------------------------------------------")
            book.seek(0)  # Resets the variable that goes through the file
            # back to 0 so that it can be iterated through again
        self.dump()

    def dump(self):
        index = open("index.txt", "w")  # Opens a new file to which every
        # keyword and its value are printed to.
        for i in self.indextree:
            line = i
            line += ": "
            line += str(self.indextree[i])
            line += "\n"
            line = line.replace('[',"")
            line = line.replace(']',"")
            index.write(line)