from load_map_ import load_map
from movement import *

def starting_UI():
    print("Welcome to ATTACK DAT SQUIRREL, a zork-inspired game designed by Tracy Xue and Ruojia Zhang")
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
    print("Good Choice! GET READY TO FIGHT ;)")

starting_UI()