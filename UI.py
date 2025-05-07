from load_map_ import load_map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
map = []
check = None

def find_start_location(map: list[list[int]]) -> tuple[int, int] | None:
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == 1:
                return (row_index+1, col_index+1)
    return None

def setLocation(x, y) -> bool:
    print(map)
    location = getCurrentLocation(map)
    print(location)

    if location is None:
        print("Current location not found. Cannot set new location.")
        return False

    previous_x = location[0]  # Convert from 1-based to 0-based indexing
    previous_y = location[1]

    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        if map[x - 1][y - 1] == 1 or map[x - 1][y - 1] == 3:
            print(f"Teleportation successful, you are now at ({x}, {y})")
            map[previous_x - 1][previous_y - 1] = 1
            map[x - 1][y - 1] = 3
            print(map)
            return True
        else:
            print("Location unavailable.")
            return False
    else:
        print("Invalid coordinates.")
        return False

def getCurrentLocation(map) -> tuple:
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == 3:
                return row_index+1, col_index+1
    return None  # If no 3 is found

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
            answer = canGoNorth()
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

        elif user_command == "teleport":
            print(map)
            x_coord = input("Which x position would you like to go? ")
            y_coord = input("Which y position would you like to go? ")
            x = int(x_coord)
            y = int(y_coord)
            print(x,y)
            success = setLocation(x, y)
            if success:
                print("Teleportation successful.")
                print(map)
            else:
                print("Teleportation failed. Invalid or blocked location.")
        else:
            print("Invalid input")
        
        """elif user_command == "go north":
            location = goNorth()
            print(location)"""


Starting_UI()
