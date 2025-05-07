from load_map_ import load_map
"""
from colorama import init, Fore, Style
previous_positions = []
# make a global variable for map
"""
map = []
previous_locations = []
x = 0
y = 0

# returns player's current location as an (x,y) tuple
def getCurrentLocation(map) -> tuple:
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == 3:
                return row_index+1, col_index+1
    return None  # If no 3 is found

def find_start_location(map: list[list[int]]) -> tuple[int, int] | None:
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == 1:
                return (row_index+1, col_index+1)
    return None

# Takes player to new location. Returns True if successful, false otherwise
"""def setLocation(x,y) -> bool:'''
    location = getCurrentLocation(map)
    print(location)
    previous_x = location[0] # Convert from 1-based to 0-based indexing
    previous_y = location[1]
    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        if map[x-1][y-1] == 1 or map[x-1][y-1] == 3:
            print(f"Teleportation successful, you are now at ({x}, {y})")
            map[previous_x-1][previous_y-1] = 1
            map[x-1][y-1] = 3
            print(map)
            return True
        else:
            print("Location unavailable.")
            return False
    else:
        print("Invalid coordinates.")
        return False"""

def setLocation(x, y) -> bool:
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
    
# print goal reached once player had arrived at the final destination
def goalReached() -> bool:
    current_map = map
    for row in current_map:
        if 2 in row:
            print("Ouch, You have not found Mr.KBLALA yet")
            return False
    print("you have found Mr.KBLALA! Get ready to fight!")
    return True

def canGoNorth(map) -> bool:
    location = getCurrentLocation(map)
    print(location)
    x = location[0] - 1 # Convert from 1-based to 0-based indexing
    y = location[1] - 1
    if 1 <= x < len(map) and 0 <= y < len(map[0]):
        if map[x - 1][y] == 1 or map[x - 1][y] == 2:
            return True  # able to go north
    return False  # either out of bounds or blocked (i.e.: 0)
    
def canGoSouth(map) -> bool:
    location = getCurrentLocation(map)
    print(location)
    x = location[0] - 1 # Convert from 1-based to 0-based indexing
    y = location[1] - 1
    if 0 <= x < len(map) - 1 and 0 <= y < len(map[0]):
        if map[x + 1][y] == 1 or map[x + 1][y] == 2:
            return True
    return False

def canGoEast(map) -> bool:
    location = getCurrentLocation(map)
    print(location)
    x = location[0] - 1 # Convert from 1-based to 0-based indexing
    y = location[1] - 1
    if 0 <= x < len(map) and 0 <= y+1 < len(map[0]):
        if map[x][y+1] == 1 or map[x][y+1] == 2:
            return True  # able to go east
    return False  # either out of bounds or blocked (i.e.: 0)

def canGoWest(map) -> bool:
    location = getCurrentLocation(map)
    print(location)
    x = location[0] - 1 # Convert from 1-based to 0-based indexing
    y = location[1] - 1
    if 0 <= x < len(map) and 1 <= y < len(map[0]):
        if map[x][y-1] == 1 or map[x][y-1] == 2:
            return True  # able to go west
    return False  # either out of bounds or blocked (i.e.: 0)

"""def goNorth():
    global map, previous_locations
    x, y = getCurrentLocation()
    if x > 0 and map[x - 1][y] in [1, 2]:
        map[x][y] = 1  # Set old position to 1
        previous_locations.append((x, y))  # add old position to previous_positions list
        x -= 1
        map[x][y] = 3  # Set new position
        return (x,y)

def goSouth():
    global map, previous_locations
    x, y = getCurrentLocation()
    if x < len(map) - 1 and map[x + 1][y] in [1, 2]:
        map[x][y] = 1  # Set old position to 1
        previous_locations.append((x, y))  # add old position to previous_positions list
        x += 1
        map[x][y] = 3  # Set new position

def goEast():
    global map, previous_locations
    x, y = getCurrentLocation()
    if y < len(map[0]) - 1 and map[x][y + 1] in [1, 2]:
        map[x][y] = 1  # Set old position to 1
        previous_locations.append((x, y))  # add old position to previous_positions list
        y += 1
        map[x][y] = 3  # Set new position

def goWest():
    global map, previous_locations
    x, y = getCurrentLocation()
    if y > 0 and map[x][y-1] in [1, 2]:
        map[x][y] = 1  # Set old position to 1
        previous_locations.append((x, y))  # add old position to previous_positions list
        y -= 1
        map[x][y] = 3  # Set new position"""