from blessed import Terminal
import time
import load_map_ as lm


term = Terminal()
game_map = lm.load_map("map1.txt")

tile_symbols = {
    '0': '█',   # wall
    '1': ' ',   # path
    '2': '✪'    # goal
}

def draw_map():
    with term.location():
        for y, row in enumerate(game_map):
            for x, char in enumerate(row):
                symbol = tile_symbols.get(str(char), '?')
                print(term.move_xy(x, y) + symbol, end='', flush=True)


squirrel_art = [
    r"   (\__/)",     # ears and head
    r"   (•ㅅ• )",     # face
    r"  / 　 づ"       # body and tail
]

def draw_squirrel(x, y):
    with term.location():
        for i, line in enumerate(squirrel_art):
            print(term.move_xy(x, y + i) + term.bright_yellow + line + term.normal)

def squirrel_scene():
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear())
        print(term.move_xy(5, 2) + "A squirrel attacks you!")
        draw_squirrel(5, 4)
        time.sleep(3)



def squirrel_battle():
    print(term.clear())
    draw_map()

    y = len(game_map) + 1  # message starts below the map
    #print(term.move_xy(5, y) + "A squirrel attacks you!")
    time.sleep(5)
    squirrel_scene()
    time.sleep(5)
    print(term.move_xy(5, y) + "Do you want to fight? (y/n)")
    while True:
        key = term.inkey()
        if key.lower() == 'y':
            print(term.move_xy(5, y + 1) + "You scared it off with your bravery!")
            break
        elif key.lower() == 'n':
            print(term.move_xy(5, y + 1) + "You lost to the squirrel")
            break
        else:
            print(term.move_xy(5, y + 2) + "Please press 'y' or 'n'")
    time.sleep(5)
    

# Example usage
if __name__ == "__main__":
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        squirrel_battle()


