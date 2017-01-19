# lab2.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Data Structures, Spring 2015
# Parkland College
# Supply the function bodies for the following functions.

def larger_square_sum(a, b, c):
    '''Returns the sum of the squares of the two larger numbers.'''
    # Formated so that it firsts checks to see if one is bigger than the other two, than it checks to see which of the
    # other two is the biggest and then performs the arithmetic

    if a > b or a > c:
        if b > c:
            data = (b**2) + (a**2)
        elif c > b:
            data = (c**2) + (a**2)
    elif b > a or b > c:
        if a > c:
            data = (a**2) + (b**2)
        elif c > a:
            data = (c**2) + (b**2)
    elif c > a or c > b:
        if a > b:
            data = (a**2) + (c**2)
        elif b > a:
            data = (b**2) + (c**2)
    return data


def hypotenuse(a, b):
    '''Returns the hypotenuse of a right triangle given legs a and b.'''
    # The variable c_squared is used to store the values of C^2 and then the math function sqrt is used to get the length
    # of the hypotenuse

    c_squared = ((a*a) + (b*b))
    import math
    return math.sqrt(c_squared)


def descriptive_stats(data):
    '''Returns the mean and median of a Python list.'''
    # for the mean I used a junk variable thats only use is to store the sum of the values of the list until every value
    # is read in, then another variable(true_mean) is then used to store the value of the first variable(pre_mean)dvided
    # by the length of the list to get the mean.
    # for the median I began by checking to see if the list was even, if not than I knew that the median could be found
    # by using integer division to find the middle of the index by dividing the length in half wich would then round down
    # and return the middle of the index. Nothing further would be needed so the loop ends.
    # if the list is even than that means that there is no middle number that would have the same amount of numbers on
    # either side of it, therefore the only way to find the median is to do integer division on the length and subtract
    # one to find the index that is halfway through the list and then add that and the one before it and then use true
    # division to find the average of those two numbers and that is the median of an even list.

    i = 0
    pre_mean = 0
    while i < len(data):
        pre_mean += data[i]
        i += 1
    true_mean = (pre_mean/len(data))

    if len(data) % 2 != 0:
        median = data[(len(data)//2)]
    else:
        median = data[(len(data)//2)-1] + data[(len(data) // 2)]
        median /= 2
    return true_mean, median


def sum_cubes_less(n):
    '''Return the sum of the cubes of the positive integers less than n.'''
    # I simply went to the number N and began at 1 and used an iterator to simply cube the number and add it to a var
    # whose only job was to store the sum of those cubes.

    i = 0
    total = 0
    while i < n:
        total += (i**3)
        i += 1
    return total


def letter_count(s):
    '''Returns a dictionary of the letters in a string where
    the keys are the individual letters and the values are the numbers of time
    that letter appears in the string.'''
    # I began by creating an empty dictionary, the one that would be returned, then i made sure that the string was in
    # all lowercase letters and searched through the string using an iterator. Within the loop i used a if statement
    # to check if the current letter was already within the dictionary, if it was i used a second dictionary to store
    # a copy of the letter with an updated count of how many there would be. Then i used the update method to update the
    # entry in the main dictionary to match the new information. If it was not already in the dictionary i simply
    # created a new entry and set the count to 1

    counter = dict()
    i = 0
    s = s.lower()
    while i < len(s):
        if s[i] in counter:
            updater = {s[i]: counter[s[i]] + 1}
            counter.update(updater)
        elif s[i] != ' ':
            counter[s[i]] = 1
        i += 1
    return counter


def dot_product(a, b):
    '''Given two lists of the same length, return the dot product as a list.
    That is, c[i] = a[i] * b[i], for all the elements in a and b.'''
    # This function simply uses an iterator to go through both lists and multiply them together in a junk var and then
    # add the result to a third list that is then returned at the end of the function.

    i = 0
    data = list()
    while i < len(a):
        junk = a[i] * b[i]
        data.append(junk)
        i += 1
    return data

if __name__ == '__main__':
    print('----Testing larger_square_sum----')
    print(larger_square_sum(5, 4, 7))
    print(larger_square_sum(2**5, 5**2, 3**2))

    print('----Testing hypotenuse----')
    print(hypotenuse(5, 12))
    print(hypotenuse(1, 1))

    print('----Testing descriptive_stats----')
    print(descriptive_stats([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(descriptive_stats([x**2 for x in range(20)]))

    print('----Testing sum_cubes_less----')
    print(sum_cubes_less(2**8))

    print('----Testing letter_count----')
    address = 'Four score and seven years ago our fathers brought forth on this'
    print(letter_count(address))

    print('----Testing dot_product----')
    print(dot_product([1, 2, 3], [-4, 5, -8]))
    print(dot_product([15, 2, -8], [2, -5, 17]))

