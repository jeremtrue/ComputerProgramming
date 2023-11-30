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

    def getphrases():
        idk2 = [
            ['You awaken in a dark cave.', 'Get up and jump around with joy.', 'Get up cautiasly', 'Lay there in agony.', 1],
            ['You wake up in the back of a wagon.', 'You scream and jump out.', 'Wake up but sit there silently.', 'Sit up and look around.', 2],
            ['You burst awake to find yourself in the middle of a dark room.', 'Sit there and look around.', 'Get up and walk around.', 'Wait to see what happens.', 3] 
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

    def story(part):
        if part == 1.1:
            print('You jump around with joy, You start to hear some voices in the distant. ')
        if part == 1.2:
            print('You get up cautially, you notice a dimly lit light in the background. ')
        if part == 1.3:
            print('You lay there, thinking...thinking....thinking...')
        if part == 2.1:
            print('You scream, and jump out of the wagon. You land harshly on a dirt trail. ')
        if part == 2.2:
            print('You burst awake, not making a peep, you start obserbing your surroundings. ')
        if part == 2.3:
            print('You wake up and slowly sit up, unaware of whats happening. Your trying to process it all. ')
        if part == 3.1:
            print('Look around.')
        if part == 3.2:
            print('Dance to the macerena. ')
        if part == 3.3:
            print('Get up and look around. ')


class Game(Initialize):
    def __init__(self):
        self.gamestart()
    
    def gamestart(self):
        # Starting the journey
        phrase = Initialize.getphrases()
        print(f'\n')
        print(phrase[0])
        Player.level += 1
        Initialize.option(phrase[1], phrase[2], phrase[3])
        choice = int(input('\nWhat is your choice? '))
        if phrase[4] == 1:
            if choice == 1:
                Initialize.story(1.1)
                Initialize.option('Get quite and hide.', 'stop talking and observe', 'Start yelling at them to help you.')
                choice = int(input('Whats your choice? '))
            elif choice == 2:
                Initialize.story(1.2)
            elif choice == 3:
                Initialize.story(1.3)
        if phrase[4] == 2:
            if choice == 1:
                Initialize.story(2.1)
            elif choice == 2:
                Initialize.story(2.2)
            elif choice == 3:
                Initialize.story(2.3)
        if phrase[4] == 3:
            if choice == 1:
                Initialize.story(3.1)
            if choice == 2:
                Initialize.story(3.2)
            if choice == 3:
                Initialize.story(3.3)
        
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

    def loadsave(self):
        Player.damage, Player.first, Player.health, Player.level, Player.enelost, Player.enewon, Player.inventory, Player.levelinprog, Player.name = self.load()

    def load(self):
        try:
            with open('save.json', 'r') as file:
                data = json.load(file)

                name = data['character']['name']
                health = data['character']['health']
                damage = data['character']['damage']
                enelost = data['character']['combat']['enelost']
                enewon = data['character']['combat']['enewon']
                inventory = data['character']['inventory']['inventory']
                first = data['character']['first']
                level = data['character']['level']

                return damage, first, health, level, enelost, enewon, inventory, name
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None, None, None, None, None, None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None, None, None, None, None
