# lab1.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

def fahrenheit_to_celsius(data): #This function is meant to convert temps in fahrenheit to celsius
        i = 0 #This is to be the iterator for the while loop that converts the converted value
        output = list()
        while i < len(data):
            junk = (data[i] - 32) * (5/9) #Coversion formula
            output.append(junk)
            i += 1
        return output #List that is returned to the user
