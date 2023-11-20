import os
import random as rand


class Game:
    def __init__(self):
        self.player = self.Player()

    
    class Initialize:
        def __init__(self):
            self.name = input("What is your characters name?")
            phrases = self.getphrases()
            enename = self.getnames()

        def getphrases(self):
            idk2 = ['You awaken in a dark cave.',
                    'You wake up in the back of a wagon.',
                    'You burst awake to find yourself in the middle of a dark room.']
            self.situation1 = rand.choice(idk2)
        def getnames(self):
             idk1 = ['Gorlock The Destoryer', 'Bob the Destoryer', 'Totally Inncent Person']
             self.monstername = rand.choice(idk1)

    class Save:
        def __init__(self):
            self.exists = self.Exists()
            self.first = 0
        class Exists:
            def __init__(self):
                self.first = 0 
                self.health = 0
                self.damage = 0
                self.level = 0
                self.enelost = 0
                self.enewon = 0
                self.inventory = 0

        class Load:
            def __init__(self):
                pass #CHANGE THIS

    class Player:
        def __init__(self):
            self.health = 0
            self.weapons = []
            self.inventory = {}
            self.movementspeed = 1
            self.points = 0
            self.level = 0
    
 #   class Start:
  #      def __init__(self):
  #          Game.Initialize.getphrases()
   #     def gamefunc():
 #           print(Game.Initialize.situation1)