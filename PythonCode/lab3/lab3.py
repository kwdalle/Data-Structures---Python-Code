# lab3.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

# For the following code fragments:
# 1. Add a comment stating the Big O performance
# 2. Add comments explaining your reasoning

# Fragment 1
k = 0
for i in range(n):  # executed n times
    for j in range(n):  # executed n times
        k = 2 + 2
# Big O(n^2)
# I believe it is n^2 since for every time the outer loop is executed then the
# inner loops is executed n times, and because the outer loop is executed n
# times this comes out to n*n = n^2

# Fragment 2
r = 0
for i in range(n):  # executed n times
    for j in range(i+1, n):  # executed (n-i) times simplifies to n times
        for k in range(i, j):  # executes n times
            r += 1
# Big O(n^3)
# I believe that it is n^4 since the first and last loop seem to be executing n
# times and the second one is doing ever smaller executions starting at (n-1)
# and going down to 1 call so to add all those up it would be (n+i) times
# making that loop n and then the total of the nested loop will be n^3


# Fragment 3
i = n
while i > 0:
    k = 2 + 2
    i = i // 2  # Divides input in half so it nuns n/2 times
# Big O(log(n))
# i is the input and because it is being divided in half every time that makes
# the algorithm logarithmic

# Fragment 4
for i in range(n):  # Executes n times
    for j in range(n):  # Executes n times
        for k in range(n):  # Executes n times
            k = 2 + 2
# Big 0(n^3)
# all three loops are executes n times so the time equals n*n*n = n^3

# Fragment 5
for i in range(n):  # executes n times
    k = 2 + 2
for j in range(n):  # executes n times
    k = 2 + 2
for k in range(n):  # executes (n-5) times
    k = 2 + 2

# Big 0(n)
# The first loop executes n times the second executes n times and the third
# executes (n-5) times so that equals n + n + (n-5) = 3n -5 which simplifies
# down to just n


def recursive_factorial(n):  # executed 1 time
    if n == 0:
        return 1  # executed once
    else:
        return n * recursive_factorial(n-1)  # executed n  times

    # Big O(n)
    # The function is called a total of n + 1 times and the operations within
    # are all O(1) so the total would be 1 + (n + 1) which simplifies to 0(n)


def tail_recursive_factorial(n, __tracker=None):  # executed 1 time
    if n == 0 or n == 1:
        if __tracker is None:
            return 1  # executed once
        else:
            return __tracker    # executed once
    elif n != 0 and __tracker is None: # This block is used initialize the trac
                                       # ker once and the recursive call is only
                                       # ever called once so it is 0(1)
        __tracker = n
        __tracker *= (n-1)
        return tail_recursive_factorial(n-1, __tracker)  # executed once
    else:
        __tracker *= (n-1)

        return tail_recursive_factorial(n-1, __tracker)  # executed n times

    # Big O(n)
    # Similar to the non tail recursive one the total calls is n and each
    # call does a constant amount of work so the total time would be n which
    # means it is O(n)