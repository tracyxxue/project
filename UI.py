from load_map_ import load_map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
map = []
check = None

def Starting_UI() -> None:
    print("Welcome.")
    while True:
        start = input("Choose a level (easy / medium / hard): ")
        if start == "easy":
            map = load_map(("map1.txt"))
            for row in map:
                print(row)
            print("Good Choice")
            break
        elif start == "medium":
            map = load_map(("map2.txt"))
            print("Good Choice")
            break
        elif start == "hard":
            map = load_map(("map3.txt"))
            print("Good Choice")
            break
        else:
            print("Invalid choice. Please try again.")
    print("few tips:")
    start_location = find_start_location(map)
    print("your start location is: ", start_location)
    check = True
    while check:
        user_command = input("Enter a command: ")
        if user_command == "hi":
            print("hi")
        elif user_command == "north?":
            answer = canGoNorth()
            if answer == True:
                print("yes")
            if answer == False:
                print("no")
        elif user_command == "south?":
            answer = canGoSouth()
            if answer == True:
                print("yes")
            if answer == False:
                print("no")
        elif user_command == "east?":
            answer = canGoEast()
            if answer == True:
                print("yes")
            if answer == False:
                print("no")
        elif user_command == "west?":
            answer = canGoWest()
            if answer == True:
                print("yes")
            if answer == False:
                print("no")
        elif user_command == "go north":
            location = goNorth()
            print(location)

        elif user_command == "teleport":
            x_coord = input("Which x position would you like to go? ")
            y_coord = input("Which y position would you like to go? ")
            try:
                x, y = int(x_coord), int(y_coord)
                setLocation(x, y)
                print(map)
            except ValueError:
                print("Invalid coordinates. Please enter two integers.")
        else:
            print("Invalid input")

Starting_UI()
