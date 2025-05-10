from blessed import Terminal
import time
import movement as m

term= Terminal()
def squirrel_attack_animation():
    squirrel = [
        [" (\\__/)", 
         " (•ㅅ•)", 
         " / 　 づ"],
                                # list of squirrels for the attack animation
        [" (\\__/) ", 
         " (•ㅅ•)💥", 
         " /　  づ"],

        [" (\\__/)💥", 
         " (•ㅅ•)", 
         " /　  づ"],

    ]
    print(term.clear())
    print ("You've reached the end of the maze, and...")
    print(term.move_xy(5, 2) + "The squirrel, Mr.KBLALA, attacks you!")
    for i in range(3):  # Loop animation for 3 times
        for s, item in enumerate(squirrel):
            for i, line in enumerate(item):
                print(term.move_xy(5, 5 + i) + term.peru + line+ term.noraml) 
                #print the squirrel graphic in squirrel color line by line
            time.sleep(0.5)




def squirrel_battle():
    squirrel_attack_animation()
    #print(term.clear())         
    print(term.white+"There is a treasure box nearby, and in it there are three bags"+term.noraml)
    print("Type 1/2/3 to choose the bag you want")
    key = term.inkey() 
    while True:
        if str(key) == "1":
            print(term.clear())
            print(term.move_xy(5, 1)+"You've found a brick in the bag")
            for i in range(3):
                print(term.move_xy(1+i, 1)+"🧱"+term.normal)
                time.sleep(0.5)
            print("You scared it off with the brick! 🥳 Congrats, you win the game!")
            break
        elif str(key) == "2":
            print(term.clear())
            print(term.move_xy(7, 1)+"There is a firecracker! You exploded the bag!")
            for i in range(3):
                print(term.move_xy(1+i, 1)+"🧨"+term.normal)
                time.sleep(0.5)
            print(term.move_xy(4, 1)+"💥"+term.normal)
            print("You have no weapon to fight Mr.KBLALA with.")   
            print("Mr.KBLALA seized Haverford, 😵 you lost...")
            break
        elif str(key) == "3":
            print(term.clear())
            print(term.move_xy(6, 1)+"It’s a trap!The squirrel bites you!")
            for i in range(3):
                print(term.move_xy(1+i, 1)+"😡"+term.normal)
                time.sleep(0.5)
            print("Mr.KBLALA seized Haverford, 😵 you lost...")
            break
        else:
            print("Invalid choice. Please type 1, 2, or 3.")
        
        time.sleep(5)

if __name__ == '__main__':
    # prevent squirrel battle to be triggered when imported
    pass                   