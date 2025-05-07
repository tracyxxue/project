from load_map_ import load_map
import game_state
from game_state import map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
check = None


def Starting_UI() -> None:
    print("Welcome.")
    while True:
        start = input("Choose a level (easy / medium / hard): ")
        if start == "easy":
            game_state.map[:] = load_map("map1.txt")  # This updates the list in place
            for row in game_state.map:
                print(row)
            print("Good Choice")
            break
        elif start == "medium":
            game_state.map[:] = load_map("map2.txt")
            print("Good Choice")
            break
        elif start == "hard":
            game_state.map[:] = load_map("map3.txt")
            print("Good Choice")
            break
        else:
            print("Invalid choice. Please try again.")
    print("few tips:")
    
    start = find_start_location(map)
    if start:
        row, col = start
        map[row-1][col-1] = 3

    print("your start location is: ", start)

    for row in map:
        print(row)
    check = True

    while check:
        user_command = input("Enter a command: ")

        if user_command == "hi":
            print("hi")

        elif user_command == "north?":
            answer = canGoNorth(map)
            if answer == True:
                print("yes")
            if answer == False:
                print("no")

        elif user_command == "south?":
            for row in map:
                print(row)
            answer = canGoSouth(map)
            if answer == True:
                print("yes")
            if answer == False:
                print("no")

        elif user_command == "east?":
            answer = canGoEast(map)
            if answer == True:
                print("yes")
            if answer == False:
                print("no")

        elif user_command == "west?":
            answer = canGoWest(map)
            if answer == True:
                print("yes")
            if answer == False:
                print("no")
        
        elif user_command == "go north":
            if goNorth():
                print("Moved north.")
            else:
                print("Cannot go north.")

        elif user_command == "go south":
            if goSouth():
                print("Moved south.")
            else:
                print("Cannot go south.")

        elif user_command == "go east":
            if goEast():
                print("Moved east.")
            else:
                print("Cannot go east.")

        elif user_command == "go west":
            if goWest():
                print("Moved west.")
            else:
                print("Cannot go west.")

        elif user_command == "teleport":
            print(map)
            x_coord = input("Which x position would you like to go? ")
            y_coord = input("Which y position would you like to go? ")
            x = int(x_coord)
            y = int(y_coord)
            print(x,y)
            success = setLocation(x,y)
            if success:
                print("Teleportation successful.")
                print(map)
            else:
                print("Teleportation failed. Invalid or blocked location.")
        else:
            print("Invalid input")


Starting_UI()
