from blessed import Terminal
import time
import movement as m

term= Terminal()
symbols_list = {'0': '█', '1': '█',  '2': '★'}

def progressive_map():
    game_map=m.tentative_map
    for x, row in enumerate(game_map):
        for y, col in enumerate(row):
            game_map[x][y]=0

    locations=m.previous_positions
    for i, row in enumerate(locations):
        for m, col in enumerate (row):
            game_map[row][col]=1
    return game_map

game_map=[[0,1,0], [0,1,0],[0,2,0]]

def draw_map():
    #game_map=progressive_map()
    print(term.clear())
    for y, row in enumerate(game_map):
        for x, item in enumerate(row):
            symbol = symbols_list.get(str(item))
            if item==1:
                print(term.move_xy(x+5,y+5) + term.red+ symbol + term.normal) 
            else:
                print(term.move_xy(x+5,y+5) + symbol)
    time.sleep(1)

draw_map()