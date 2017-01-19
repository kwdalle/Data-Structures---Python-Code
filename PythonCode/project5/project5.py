# project5.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

from itinerary import *
from graph import *
from string import *

itinerary = Itinerary()

vertices = itinerary.get_vertices()
answer = 'y' #Insures that the loop starts.

while answer == "y" or answer == "Y":
    v1 = input("Enter your origination: ").lower()
    v2 = input("Enter your destination: ").lower()
    if v1 in vertices.keys() and v2 in vertices.keys():
        v1 = vertices[v1] #Looks up the vertex object to be sent to build the
                          # trip plan.
        v2 = vertices[v2]

        path, time = itinerary.plan(v1,v2)
        if path != None and time != None: #Checks to see if the were connected.
            time *= 60 #Converts the time given to hours and minutes
            hours = time // 3600
            minutes = time // 60 - hours * 60

            print("The shortest plan is as follows")

            i = 0
       
            while i < len(path): #Loops over the path variable to print it and 
                             #give the correct path from start to finish.
                print(str(path[i]).capitalize())
                i += 1
            print("Hours:", hours, "  Minutes:", minutes)
        else:
            print("Your destination and origination are not connected\n")
    else: #Checks to make sure you entered valid locations.
        if v1 not in vertices.keys() and v2 not in vertices.keys():
            print("Your origination and destination are not in the Eurail",
                  "system.")
            v1 = ""
            v2 = ""
        elif v1 not in vertices.keys():
            print("Your origination is not in the Eurail system.")
            v1 = ""
        else:
            print("Your destination is not in the Eurail system.")
            v2 = ""

    answer = input("Would you like to look at another two cities? Y/N\n")

input = input("Would you like to dump the current itinerary to a Viz file? Y/N\n")

if input == "y" or input == "Y":
    if v1 != "" and v2 != "": 
        itinerary.write_file(path)
    else: #Checks to make sure that at one point you entered valid locations.
        print("Sorry you recently did not enter an valid itinerary :D")