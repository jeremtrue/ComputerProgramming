import json
import random as rand

class Initialize:
    def __init__(self):
        # Instantiate the Game class
        self.name = self.getcharname()
        self.dirque()
        

    def printdir(self):
        print('\nHow to play:')
        print('First, you would enter your name')
        print('Next, you would start your journey.')
        print('When you are asked a yes or no question, just type y/n or yes/no.')
        print('When you are asked to input a number from a chart, just type the number next to your answer.\n')
        firstque = input('Do you understand? y/n: ')
        if firstque == 'y' or firstque == 'yes':
            print('Great! Good luck')
        else:
            print('Well then, you see, I have no clue. Good luck!\n')

    def getcharname(self):
        name = str(input("\nWhat is your Character's name? "))
        return name

    def getphrases(self):
        idk2 = [
            ['You awaken in a dark cave.', ],
            'You wake up in the back of a wagon.',
            'You burst awake to find yourself in the middle of a dark room.'
            ]
        return rand.choice(idk2)

    def getnames(self):
        idk1 = ['Gorlock The Destroyer', 'Bob the Destroyer', 'Totally Innocent Person']
        return rand.choice(idk1)

    def dirque(self):
        firstque = input('\nDo you need instructions? y/n: ')
        if firstque == 'y' or firstque == 'yes':
            self.printdir()
        else:
            print('\nWell then, you see, I think you need them!')
            self.printdir()

    def option(o1, o2, o3):
        print('\nPick you move.')
        print(f'1\t{o1}')
        print(f'2\t{o2}')
        print(f'3\t{o3}')

class Game(Initialize):
    def __init__(self):
        self.gamestart()
    
    def gamestart(self):
        # Starting the journey
        print(self.getphrases())
        Player.level += 1
        Initialize.option('', 'two', 'three')
        
class Player:
    damage = 0
    first = 1
    health = 0
    level = 0
    enelost = 0
    enewon = 0
    inventory = []
    levelinprog = 0
    name = ""

    def __init__(self):
        pass


class Saves:
    def __init__(self):
        pass

    filename = 'save.json'

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

                name = data['character']['name']
                health_level = data['character']['health']
                damage = data['character']['damage']
                enelost = data['character']['combat']['enelost']
                enewon = data['character']['combat']['enewon']
                inventory = data['character']['inventory']['inventory']
                return name, health_level, damage, enelost, enewon, inventory
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None, None, None, None, None, None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None, None, None, None, None

saves = Saves()
