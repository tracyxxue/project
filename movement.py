from load_map_ import load_map
"""
from colorama import init, Fore, Style
previous_positions = []
# make a global variable for map
"""
tentative_map = load_map("map1.txt")
x = 0
y = 0

# returns player's current location as an (x,y) tuple
def getCurrentLocation() -> tuple:
    column_number = 0
    row_number = 0
    current_map = tentative_map
    for row in current_map:
        if 3 not in row:
            row_number += 1
        else:
            for cell in row:
                if cell != 3:
                    column_number += 1
            break  # Once we find the row with 3, we don't need to continue
    return (column_number, row_number)

# Takes player to new location. Returns True if successful, false otherwise
def setLocation(x: int, y: int) -> bool:
    current_map = tentative_map
    previous_x, previous_y = getCurrentLocation()
    if 0 <= x < len(current_map) and 0 <= y < len(current_map[0]):
        if current_map[x-1][y-1] == 1 or current_map[x-1][y-1] == 3:
            print(f"Teleportation successful, you are now at ({x}, {y})")
            current_map[previous_x-1][previous_y-1] = 1
            current_map[x-1][y-1] = 3
            print(current_map)
            return True
        else:
            print("Location unavailable.")
            return False
    else:
        print("Invalid coordinates.")
        return False
    
# print goal reached once player had arrived at the final destination
def goalReached() -> bool:
    current_map = tentative_map
    for row in tentative_map:
        if 2 in row:
            print("Ouch, You have not found Mr.KBLALA yet")
            return False
    print("you have found Mr.KBLALA! Get ready to fight!")
    return True

def canGoNorth() -> bool:
    x, y = getCurrentLocation()
    current_map = tentative_map
    if 1 <= x < len(current_map) and 0 <= y < len(current_map[0]):
        if current_map[x - 1][y] == 1 or current_map[x - 1][y] == 2:
            return True  # able to go north
    return False  # either out of bounds or blocked (i.e.: 0)
    
def canGoSouth() -> bool:
    x, y = getCurrentLocation()
    current_map = tentative_map
    if 0 <= x < len(current_map)-1 and 0 <= y < len(current_map[0]):
        if current_map[x + 1][y] == 1 or current_map[x + 1][y] == 2:
            return True  # able to go south
    return False  # either out of bounds or blocked (i.e.: 0)

def canGoEast() -> bool:
    x, y = getCurrentLocation()
    current_map = tentative_map
    if 0 <= x < len(current_map) and 0 <= y+1 < len(current_map[0]):
        if current_map[x][y+1] == 1 or current_map[x][y+1] == 2:
            return True  # able to go east
    return False  # either out of bounds or blocked (i.e.: 0)

def canGoWest() -> bool:
    current_map = tentative_map
    x, y = getCurrentLocation()
    if 0 <= x < len(current_map) and 1 <= y < len(current_map[0]):
        if current_map[x][y-1] == 1 or current_map[x][y-1] == 2:
            return True  # able to go west
    return False  # either out of bounds or blocked (i.e.: 0)

def goNorth():
    global tentative_map, previous_positions
    x, y = getCurrentLocation()
    if x > 0 and tentative_map[x - 1][y] in [1, 2]:
        tentative_map[x][y] = 1  # Set old position to 1
        previous_positions.append((x, y))  # add old position to previous_positions list
        x -= 1
        tentative_map[x][y] = 3  # Set new position

def goSouth():
    global tentative_map, previous_positions
    x, y = getCurrentLocation()
    if x < len(tentative_map) - 1 and tentative_map[x + 1][y] in [1, 2]:
        tentative_map[x][y] = 1  # Set old position to 1
        previous_positions.append((x, y))  # add old position to previous_positions list
        x += 1
        tentative_map[x][y] = 3  # Set new position

def goEast():
    global tentative_map, previous_positions
    x, y = getCurrentLocation()
    if y < len(tentative_map[0]) - 1 and tentative_map[x][y + 1] in [1, 2]:
        tentative_map[x][y] = 1  # Set old position to 1
        previous_positions.append((x, y))  # add old position to previous_positions list
        y += 1
        tentative_map[x][y] = 3  # Set new position

def goWest():
    global tentative_map, previous_positions
    x, y = getCurrentLocation()
    if y > 0 and tentative_map[x][y-1] in [1, 2]:
        tentative_map[x][y] = 1  # Set old position to 1
        previous_positions.append((x, y))  # add old position to previous_positions list
        y -= 1
        tentative_map[x][y] = 3  # Set new position