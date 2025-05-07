from load_map_ import load_map
"""
from colorama import init, Fore, Style
previous_positions = []
# make a global variable for map
"""
import game_state
from game_state import map
previous_locations = []
x = 0
y = 0

# returns player's current location as an (x,y) tuple
def getCurrentLocation():
    for row_index, row in enumerate(game_state.map):
        for col_index, value in enumerate(row):
            if value == 3:
                return row_index, col_index
    return None
getCurrentLocation()

def print_map():
    for row in game_state.map:
        print(row)

def find_start_location(map: list[list[int]]) -> tuple[int, int] | None:
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == 1:
                return (row_index+1, col_index+1)
    return None

# Takes player to new location. Returns True if successful, false otherwise
import game_state

def setLocation(x, y) -> bool:
    location = getCurrentLocation()
    if location is None:
        print("Current location not found.")
        return False
    previous_x, previous_y = location  # Already 0-based
    # Ensure x and y are 1-based from user, so convert to 0-based for map access
    x0, y0 = x - 1, y - 1
    # Check if the new coordinates are in bounds
    if 0 <= x0 < len(game_state.map) and 0 <= y0 < len(game_state.map[0]):
        if game_state.map[x0][y0] in [1, 3]:
            # Reset old location to 1
            game_state.map[previous_x][previous_y] = 1
            previous_locations.append((previous_x+1, previous_y+1))
            print("previous locations are: ", previous_locations)
            # Set new location to 3
            game_state.map[x0][y0] = 3
            print(f"Teleportation successful, you are now at ({x}, {y})")
            for row in game_state.map:
                print(row)
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
    location = getCurrentLocation() #0-based coordinates
    print(location)
    x = location[0]
    y = location[1]
    if 1 <= x < len(map) and 0 <= y < len(map[0]):
        if map[x - 1][y] == 1 or map[x - 1][y] == 2:
            return True  # able to go north
    return False  # either out of bounds or blocked (i.e.: 0)
    
def canGoSouth(map) -> bool:
    location = getCurrentLocation()
    print(location)
    x = location[0]
    y = location[1]
    if 0 <= x < len(map) - 1 and 0 <= y < len(map[0]):
        if map[x + 1][y] == 1 or map[x + 1][y] == 2:
            return True
    return False

def canGoEast(map) -> bool:
    location = getCurrentLocation()
    print(location)
    x = location[0]
    y = location[1]
    if 0 <= x < len(map) and 0 <= y+1 < len(map[0]):
        if map[x][y+1] == 1 or map[x][y+1] == 2:
            return True  # able to go east
    return False  # either out of bounds or blocked (i.e.: 0)

def canGoWest(map) -> bool:
    location = getCurrentLocation()
    print(location)
    x = location[0]
    y = location[1]
    if 0 <= x < len(map) and 1 <= y < len(map[0]):
        if map[x][y-1] == 1 or map[x][y-1] == 2:
            return True  # able to go west
    return False  # either out of bounds or blocked (i.e.: 0)

def goNorth():
    location = getCurrentLocation()
    if location is None:
        print("Current location not found.")
        return None

    x, y = location
    if x > 0 and game_state.map[x - 1][y] in [1, 2]:
        game_state.map[x][y] = 1  # Clear old position
        previous_locations.append((x+1, y+1))  # Track history
        print(previous_locations)
        x -= 1
        game_state.map[x][y] = 3  # Set new position
        return (x, y)
    else:
        print("You can't go north.")
        return None

def goSouth():
    location = getCurrentLocation()
    if location is None:
        print("Current location not found.")
        return None

    x, y = location
    if x < len(game_state.map) - 1 and game_state.map[x + 1][y] in [1, 2]:
        game_state.map[x][y] = 1
        previous_locations.append((x+1, y+1))
        print(previous_locations)
        x += 1
        game_state.map[x][y] = 3
        return (x, y)
    print("You can't go south.")
    return None

def goEast():
    location = getCurrentLocation()
    if location is None:
        print("Current location not found.")
        return None

    x, y = location
    if y < len(game_state.map[0]) - 1 and game_state.map[x][y + 1] in [1, 2]:
        game_state.map[x][y] = 1
        previous_locations.append((x+1, y+1))
        print(previous_locations)
        y += 1
        game_state.map[x][y] = 3
        return (x, y)
    print("You can't go east.")
    return None

def goWest():
    location = getCurrentLocation()
    if location is None:
        print("Current location not found.")
        return None

    x, y = location
    if y > 0 and game_state.map[x][y - 1] in [1, 2]:
        game_state.map[x][y] = 1
        previous_locations.append((x+1, y+1))
        print(previous_locations)
        y -= 1
        game_state.map[x][y] = 3
        return (x, y)
    print("You can't go west.")
    return None