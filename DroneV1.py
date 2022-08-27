import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog
from docx2txt import docx2txt
import pathlib

print("Welcome to Drone Tracking Software")

#Function to ask if there is another route
def replay():
    return input('Do you have another Route: ').lower().startswith('y')
#Function to show the Route on the map
def showRoute():
    #array that has the information in
    x = np.array(nx)
    y = np.array(ny)
    fig, ax = plt.subplots()
    plt.title("Starting Coordinates are: " + " X =  " + doc_list[0] + ", " + "Y = " + doc_list[1])
    plt.suptitle("Drone Route")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    ax.step(x, y, linewidth=2.5)
    ax.set(xlim=(0, 13), xticks=np.arange(1, 13),
           ylim=(0, 13), yticks=np.arange(1, 13))
    #adds the coordinates onto the graph
    for xy in zip(x, y):
        plt.annotate(xy, xy=xy)
    plt.grid()
    plt.show()
    #adds the coordinates to the command line
    con = np.concatenate((x,y))
    print("Route Coordinates are below:")
    print(np.vstack((x,y)).T)


while True:
    nx = []
    ny = []
    #asks for the initual route
    newRoute = input('Would you like to enter a route? Enter Yes or No:')
    if newRoute.lower()[0] == 'y':
        runRoute = True
    else:
        runRoute = False


    while runRoute == True:
        #gets the file from the input function
        filename =  input("Please enter the FilePath + FileName: ")
        file = pathlib.Path(filename)
        if file.exists():
            print("")
        else:
            print("I'm Sorry that doesnt look like a valid file path. Please try again.")
            continue

        doc_result = docx2txt.process(filename)
        doc_list = doc_result.split()

        nx = []
        ny = []
        x = int(doc_list[0])
        y = int(doc_list[1])
        nx.append(int(doc_list[0]))
        ny.append(int(doc_list[1]))
        #for loop to go  through the file content. It will update X and Y depending on if its N | S | E | W. It will then add the new number to the array
        for directions in doc_list:
            if directions == 'N':
                y = y + 1
                ny.append(y)
                nx.append(x)
                if y < 0:
                    break
                    replay()
                    
            elif directions == 'E':
                x = x + 1
                nx.append(x)
                ny.append(y)
                if x < 0:
                    break
                    replay()
        
            elif directions == 'S':
                y = y - 1
                ny.append(y)
                nx.append(x)
                if y < 0:
                    break
                    replay()
                    
            elif directions == 'W':
                x = x - 1
                nx.append(x)
                ny.append(y)
                if x < 0:
                    break
                    replay()      
            else:
                continue
        #checks if the route is invalid and will print out an error
        showTheRoute = True
        if x < 0:
            isValid = False
            errorInput = input("You have an Error in the Route Would you still like to view the route? Enter Y or N: ")
            if errorInput.lower()[0] == 'y':
                showTheRoute = True
            else:
                showTheRoute = False
        if showTheRoute == True:
            showRoute()
        else:
            replay

        if not replay():
            print("Goodbye")
            break
    break