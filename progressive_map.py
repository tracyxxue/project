from blessed import Terminal
import time
from movement import *
from game_state import map, previous_locations

term= Terminal()
symbols_list = {'0': '★ ',    # the wall is represented by stars and the traveled path represented by blocks
    '1': '░ '}

def progressive_map():
    game_map = [[0] * len(map[0]) for i in range(len(map))]    
     #initialize the map all to 0

    locations = previous_locations
    for item in locations:              #update the locations that has been traveled to 1
        row, col = item  
        game_map[row][col] = 1

    return game_map


def draw_map():
    game_map=progressive_map()
    print(term.clear())
    for y, row in enumerate(game_map):        
        for x, item in enumerate(row):
            symbol = symbols_list.get(str(item), ' ')   #print the progressive map
            if item == 1:
                print(term.move_xy(x*2, y) + term.red + symbol + term.normal)  # the path printed in red and the space
            else:                                                    # between elements doubeled for better visualization
                print(term.move_xy(x*2, y) + symbol+ term.normal)\

    time.sleep(3)
