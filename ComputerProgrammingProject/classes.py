import os
import random as rand

class Game:
    def __init__(self):
        self.player = self.Player()
    
    class Initialize:
        def __init__(self):
            self.name = input("What is your characters name?")
            print('WARNING: Saves are in development dont rely on them. Just say no if no save')
            self.ifsave = input("Do you have a save file?")
            Game.Start(self.name)
        def genphrases():
            enames = ['Gorlock The Destoryer', 'Bob the Destoryer', 'Totaly Inncent Person']
            gstart = ['You awaken in a dark cave.',
                      'You wake up in the back of a wagon.',
                      'You burst awake to find yourself in the middle of a dark room.']


    class Save:
        class Exists:
            def __init__(self):
                pass #change this too

        class Load:
            def __init__(self):
                pass #CHANGE THIS


    class Player():
        def __init__(self):
            self.health = 0
            self.weapons = []
            self.inventory = {}
            self.movementspeed = 1
            self.points = 0
            self.level = 0
    
    class Start:
        print(rand.gstart)



            

