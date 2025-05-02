from load_map_ import load_map
from movement import *
from progressive_map import *
from blessed import Terminal
import time
map = []

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
  print(goalReached())
  check=True
  while check:
    check = not goalReached()
    """user_command = input("Enter a command: ")
    if user_command == "teleport":
      coords = input("Where would you like to go? (format: x y): ")
      try:
        x_str, y_str = coords.strip().split()
        x, y = int(x_str), int(y_str)
        setLocation(x, y)
      except ValueError:
          print("Invalid coordinates. Please enter two integers separated by space.")"""
    print("hi")
    """if user_command = "North?":
      print(canGoNorth())
      if canGoNorth() is True:
        print("north")
    
    
      print(canGoNorth())
      if canGoNorth() is True:
        print("Yes you may go North.")
      else:
        print("No Road to North is blocked")
    elif user_command == "South?":
      canGoSouth()
      if canGoSouth() is True:
        print("Yes you may go South.")
      else:
        print("No Road to South is blocked")
    elif user_command == "South?":
      canGoSouth()
    elif user_command == "East?":
      canGoEast()
    elif user_command == "West?":
      canGoWest()
    elif user_command == "Go North":
      goNorth()
    elif user_command == "Go South":
      goSouth()
    elif user_command == "Go East":
      goEast()
    elif user_command == "Go West":
      goWest()
    elif user_command == "map":
      draw_map()
    else:
      print("Invalid input. Try again.")
      """
starting_UI()