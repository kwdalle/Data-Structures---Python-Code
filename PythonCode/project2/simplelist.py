# Kevin Dalle
# removed the print method and added two write faces for the vertices and
# faces respectively and added a get size and triangulation method.
# simplelist.4.py
# CSC 220 Spring 2015, Parkland College
# Version 4 - Use "private" members. If we have __Node, probably
# don't need __data and __next, but this will show you the syntax.
# Note in particular that now we have to reference the ctor using
# self.__Node(data) instead of just Node(data)

class List:
    '''A List class that just contains the head and tail references
    plus its current size. It contains an internal Node class for
    the link nodes.
    '''
    class __Node:
        '''A Node class that just contains data and a next reference.'''
        def __init__(self, data):
            self.__data = data
            self.__next = None

        def get_data(self):
            return self.__data

        def set_data(self, data):
            self.__data = data

        def get_next(self):
            return self.__next
        
        def set_next(self, next):
            self.__next = next

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add_first(self,e):
        '''Add a node to the front of the list.'''
        newest = self.__Node(e)
        newest.set_next(self.__head)
        self.__head = newest
        if self.__size == 0:
            self.__tail = self.__head
        self.__size += 1

    def add_last(self,e):
        '''Add a node to the back of the list.'''
        newest = self.__Node(e)
        newest.set_next(None)
        if self.__tail is None:
            self.__tail = newest
        self.__tail.set_next(newest)
        self.__tail = newest
        if self.__size == 0:
            self.__head = self.__tail
        self.__size += 1

    def remove_first(self):
        '''Remove a node from the front of the list.'''
        if self.__head is None:
            print("error, trying to remove from empty list.")
        else:
            tmp = self.__head
            self.__head = self.__head.get_next()
            self.__size -= 1
            tmp.set_next(None)

    def write_vertices(self, ofile):
        '''Loops through the data writing the vertices'''
        current = self.__head
        while current:
            temp = current.get_data()
            print(' '.join(str(p) for p in temp), file=ofile)
            current = current.get_next()

    def write_faces(self, ofile):
        """Loops through the data and writes the faces"""
        current = self.__head
        while current:
            i = 0
            temp = current.get_data()
            while i < len(temp):
                temp2 = int(temp[i])
                temp2 -= 1
                temp[i] = str(temp2)
                i += 1
            print(str(len(temp)), ' '.join(str(p) for p in temp), file=ofile)
            current = current.get_next()

    def triangulation(self):
        """Triangularizes the faces of a polygon"""
        current = self.__head
        j = True
        while current:
            temp = current.get_data()
            if len(temp) > 3:
                i = 1
                while i < len(temp)-1:
                    newlist = list()
                    newlist.append(int(temp[0])+1)  # appends the triangulated
                    newlist.append(int(temp[i])+1) # points to a new list
                    newlist.append(int(temp[i+1])+1)
                    i += 1  # increases the iter
                    if j is True:  # If we are at the head
                        newest = self.__Node(newlist)  # sets the newest to a
                        self.__head = newest       # a node with the new list
                        # sets the head to the newest
                        newest.set_next(current.get_next())  # sets the nxt ele
                                                            # to the curs next
                        current.set_next(None)  # sets the curs next to none
                        current = newest        # sets the cur to the newest
                        j = False  # says we are no longer at the head
                    else:
                        newest = self.__Node(newlist)  # same as above
                        old = current  # sets the current node to the old node
                        newest.set_next(old.get_next())  # sets news next to
                                                         # olds next
                        current = newest  # sets current to new
                        if len(old.get_data()) > 3:
                            old.set_next(None)  # it sets the old to point to
                                                # none
                            pred.set_next(current)  # Sets the predecessors nxt
                                                    # to the current ele
                        else:
                            old.set_next(newest)  # sets curs next to new
                    del newlist
                pred = current  # sets the predecessor to the current b4 we
                                # switch the current element
                current = current.get_next()  # gets the next element
            else:
                temp[0] = int(temp[0])+1  # makes sure that they are ready for
                temp[1] = int(temp[1])+1  # the 0 index alteration of the write
                temp[2] = int(temp[2])+1  # function
                old = current  # sets the old ele to the cur ele
                old.set_data(temp)  # updates the Data so its ready to write out
                pred = old  # sets the predecessor to the cur ele b$ updating
                current = old.get_next()  # gets the next element
        cur = self.__head  # sets cur to the head
        self.__size = 0  # sets size to 0
        while cur:  # counts the number triangle faces in the LL
            if len(cur.get_data()) == 3:
                self.__size += 1
                cur = cur.get_next()
            else:
                cur = cur.get_next()

    def get_size(self):
        """Is used to get the size for the polygon section of the triangulation
        """
        return self.__size

    def __len__(self):
        return self.__size

if __name__ == '__main__':
    # This is a minimal amount of testing, you should implement more.
    print("simplelist version 4")
    L = List()
    L.add_first('one')
    L.add_first('two')
    L.add_first('three')
    L.add_last('red')
    L.add_last('green')
    L.add_last('blue')
    L.remove_first()
    L.remove_first()
