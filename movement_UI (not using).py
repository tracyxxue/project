from load_map_ import load_map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
from game_state import map
check = None

def starting_UI():
  print("""
          **************Welcome to ATTACK DAT SQUIRREL***************
          a zork-inspired game designed by Tracy Xue and Ruojia Zhang
          ############################################################
          Once upon a time...
          the villan of the world...
          Mr.KBLALA the Black Squirrel...
          appeared on our very own lovely Haverford College...
          You are tasked to fight with Mr.KBLALA
          **Don't forget to find your weapen on your journey**
          """)

  start = input("choose your difficuly level: easy, medium, hard: ")
  if start == "easy":
    map = load_map("map1.txt") # remember to change all "tentative map" in movement.py into "map"
  if start == "medium":
    map = load_map("map2.txt")
  if start == "hard":
    map = load_map("map3.txt")
  else:
    print("invalid input.")
    start = input("choose your difficuly level: easy, medium, hard: ")
  print("""Good Choice! 
          I have a few more helpful tips for you before you pivot :)
          Your overall goal is to find Mr.KBLALA and use your weapon of choice to fight
          To teleport:
            type "teleport", then enter a coordinates that you want to travel to
          To move by grid:
            type "North?" or "South?" or "East?" or "West?" to test if you could move to your intended location
            type "Go North" or "Go South" or "Go East" or "Go West" to make your movement.
          To check where you have already traveled:
            type "map"
          GET READY TO FIGHT ;)""")
  check=True
  while check:
    user_command = input("Enter a command: ")
    if user_command == "hi":
      print("hi")
    elif user_command == "teleport":
      x_coord = input("which x position would you like to go? ")
      y_coord = input("which y position would you like to go? ")
      try:
        x, y = int(x_coord), int(y_coord)
        setLocation(x, y)
      except ValueError:
        print("invalid coordinates. please enter two integers separated by space.")
        user_command = input("Enter a command: ")
    else:
      print("invalid input")
starting_UI()