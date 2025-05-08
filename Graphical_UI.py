from blessed import Terminal
import time
import movement as m

term= Terminal()
"""
game_map=m.tentative_map
for x, row in enumerate(game_map):
     for y, col in enumerate(row):
          game_map[x][y]=0

locations=m.previous_positions
for i, row in enumerate(locations):
     for m, col in enumerate (row):
          game_map[row][col]=1



term= Terminal()
symbols_list = {'0': '█', '1': ' ',  '2': '✪'}

def draw_map():
    print(term.clear())
    for y, row in enumerate(game_map):
            for x, item in enumerate(row):
                symbol = symbols_list.get(str(item))
                if item=="1":
                    print(term.move_xy(x, y) + term.red + symbol ) 
                print(term.move_xy(x, y) + symbol)
    time.sleep(1)
"""

squirrel = [
    "   (\__/)",     
    "   (•ㅅ• )",    
    "  /    づ"      
]
term.line()                                     #print the above squirrel line by line
def draw_squirrel():
        for i, line in enumerate(squirrel):
            print(term.move_xy(5,5+i) + term.yellow + line)

def squirrel_scene():
    with term.fullscreen():      #clear the screen after the graphic is shown
        print(term.clear())
        print(term.move_xy(5, 2) + "A squirrel attacks you!")
        draw_squirrel()
        time.sleep(3)



def squirrel_battle():
    print(term.clear())
    squirrel_scene()               
    time.sleep(3)
    print(term.move_xy(5, 2) + "Do you want to fight? (y/n)") #ask the player if they want to fight
    while True:
        key = term.inkey()     #take in response from the player
        if key.lower() == 'y':
            print(term.move_xy(5,4) + "You scared it off with your bravery! Congrats, you win the game!")
            break
        elif key.lower() == 'n':
            print(term.move_xy(5, 4) + "You lost to the squirrel")        #battle with the squirrrel
            break
        else:
            print(term.move_xy(5, 5) + "Please press 'y' or 'n'")
    time.sleep(5)
    

#if m.goalReached(): 

if True:
    squirrel_battle()


