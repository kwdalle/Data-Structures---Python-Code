# project2.py
# Kevin Dalle
# kdalle1@stu.parkland.edu
# CSC 220, Spring 2015

from simplelist import *  # imports the linked list used in this project

from sys import argv  # imports argv for command arguments

ifilename = argv[1]  # takes the file name you give

ifile = open(ifilename, "r")
numfaces = 0  # will count the number of faces for the vtk conversion
numverts = 0  # does the same thing as above but for vertices
minimum = {'x': 0, 'y': 0, 'z': 0}  # just creates a dict for the min values
maximum = {'x': 0, 'y': 0, 'z': 0}  # same thing but for max
facenum = dict()  # creates a dict to hold the number of diff faces
faces = List()  # lists that will be used within the linked lists
vertices = List()
tally = 0  # will count the number of data in the polygons for the conversion
i = 1  # simply used to signify we are at the beginning of the file when
       # finding the min a max ordinates

for line in ifile:
    temp = line.split(' ')  # Splits the line by spaces and stores it in a list
    if temp[0] == 'f':  # Checks if its a face
        numfaces += 1  # adds to the face counter if it is
        j = len(temp) - 1  # the true num of points on a face
        if j in facenum:  # if its already in the dict just add one more to
                          # the count
            facenum[j] += 1
        else:  # If it was not in the dict it creates an entry
            facenum[j] = 1
        tally += (j+1)  # compounds the num of data in the polygon section
        temp.remove('f')  # removes the f as it is not needed in vtk
        faces.add_last(temp)  # adds the list to the end of the LL for faces
    elif temp[0] == 'v':  # Checks if its a vertex
        numverts += 1  # Adds to the num of vertexs
        if i == 1:  # if its at the start of a file it starts by setting all
                    # the maxs and mins to the first ones in the file
            minimum['x'] = float(temp[1])
            minimum['y'] = float(temp[2])
            minimum['z'] = float(temp[3])
            maximum['x'] = float(temp[1])
            maximum['y'] = float(temp[2])
            maximum['z'] = float(temp[3])
            i = 0  # Signifies that we are no longer at the beginning of the
                    # file
        else:  # If its not at the beginning it checks the Y's X's and Z's to
                # see if they could be the new mins or maxs
            if minimum['x'] >= float(temp[1]):
                minimum['x'] = float(temp[1])
            if minimum['y'] >= float(temp[2]):
                minimum['y'] = float(temp[2])
            if minimum['z'] >= float(temp[3]):
                minimum['z'] = float(temp[3])
            if maximum['x'] <= float(temp[1]):
                maximum['x'] = float(temp[1])
            if maximum['y'] <= float(temp[2]):
                maximum['y'] = float(temp[2])
            if maximum['z'] <= float(temp[3]):
                maximum['z'] = float(temp[3])
        temp.remove('v')  # Removes the v as its not needed in VTK
        vertices.add_last(temp)  # adds the list to the LL for vertices

ifile.close()  # closes the input file

ofilename = ifilename.replace('obj', 'vtk')  # mods the filename given by the
# user so that it is using the write file type but is otherwise the same name
#  as the original output file
ofile = open(ofilename, "w")  # opens the file
ofile.write("# vtk DataFile Version 3.0\n")  # Next three lines write the VTK
                                            # header
ofile.write("Converted by Kevin Dalle\n")
ofile.write("ASCII\n")
ofile.write("DATASET POLYDATA\n")  # starts the beginning of the vertices
                                    # section of the file
ofile.write("POINTS " + str(len(vertices)) + " float\n")  # lists the num of
                                                        # points and raw type

vertices.write_vertices(ofile)  # writes out the vertices in the VTK format
ofile.write("\n")  # writes out a new line before the face section
print("POLYGONS ", numfaces, " ", tally, file=ofile)  # writes a section that
                                                    # signifies the start of
                                                    # the Faces section
faces.write_faces(ofile)  # Writes out the faces in VTK format

ofile.close()  # closes the first output file

ofilename2 = ifilename.replace('.obj', '2.vtk')  # changes the input filename
                                                # for the triangulation file
ofile = open(ofilename2, "w")
ofile.write("# vtk DataFile Version 3.0\n")  # same 5 as above
ofile.write("Converted by Kevin Dalle(Trianglularized)\n")
ofile.write("ASCII\n")
ofile.write("DATASET POLYDATA\n")
ofile.write("POINTS " + str(len(vertices)) + " float\n")

vertices.write_vertices(ofile)  # same as before
faces.triangulation()  # triangulates the faces
ofile.write("\n")  # writes a new line between faces and vertices
print("POLYGONS ", faces.get_size(), " ", faces.get_size()*4, file=ofile)
#  prints out the number of faces and the size of the data in the section
faces.write_faces(ofile)  # writes out those faces while making sure
                                    # there is no residual 4 sized faces

ofile.close()  # closes the second output file

#  Prints out the stats table
print("Number of Faces:", numfaces)
print("Number of Vertices:", numverts)
print("Max x:", maximum['x'])
print("Max y:", maximum['y'])
print("Max z:", maximum['z'])
print("Min x:", minimum['x'])
print("Min y:", minimum['y'])
print("Min z:", minimum['z'])
print("Face Nums:", str(facenum))
