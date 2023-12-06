import json
import random as rand
import time                                                                            
class Initialize:
    def __init__(self):
        # Instantiate the Game class
        self.name = self.getcharname()
        self.dirque()

    def printdir(self):
        print('\nHow to play:')
        print('First, you would enter your name (you already did this)')
        print('Next, you would start your journey.')
        print('When you are asked a yes or no question, just type y/n or yes/no.')
        print('When you are asked to input a number from a chart, just type the number next to your answer.\n')
        time.sleep(3)
        firstque = input('Do you understand? y/n: ')
        if firstque == 'y' or firstque == 'yes':
            print('Great! Good luck')
        else:
            print('\nWell then, you see, I have no clue. Good luck!')

    def getcharname(self):
        name = str(input("\nWhat is your Character's name? "))
        return name

    def getphrases():
        idk2 = [
            ['You awaken in a dark cave.', 'Get up and jump around with joy.', 'Get up cautiasly', 'Lay there in agony.', 1],
            #['You wake up in the back of a wagon.', 'You scream and jump out.', 'Wake up but sit there silently.', 'Sit up and look around.', 2],
            #['You burst awake to find yourself in the middle of a dark room.', 'Sit there and look around.', 'Get up and walk around.', 'Wait to see what happens.', 3] 
            ]
        return rand.choice(idk2)

    def getnames(self):
        idk1 = ['Gorlock The Destroyer', 'Bob the Destroyer', 'Totally Innocent Person']
        return rand.choice(idk1)

    def dirque(self):
        firstque = input('\nDo you need instructions? y/n: ')
        time.sleep(1)
        if firstque == 'y' or firstque == 'yes':
            self.printdir()
        else:
            print('\nWell then, you see, I think you need them!')
            self.printdir()
    
    def agony(self, x):
            while x > 0:
                print('\nthinking......')
                time.sleep((rand.randint(0,3)))
                print('thinking.....')
                time.sleep((rand.randint(0,4)))
                print('thinking.....whoah........')
                time.sleep((rand.randint(0,3)))
                print('thinking.......')
                print('thinking...\tthinking')
                time.sleep((rand.randint(0,4)))
                print('\t\t\tthinking')
                time.sleep(1)
                print('\t\tthinking')
                time.sleep(1)
                print('\tthinking')
                time.sleep(1)
                x -= 1
            if x == 0:
                print('Thinking...............')
                time.sleep((rand.randint(2,3)))
                print('\now')
                

    def option(o1, o2, o3):
        print('\nPick you move.')
        print(f'1\t{o1}')
        print(f'2\t{o2}')
        print(f'3\t{o3}')

    def story(self, part):
        if part == 1.1:
            print('You jump around with joy, When all of a sudden.... You start to hear some voices in the distant. ')
        elif part == 1.2:
            print('You get up cautially, you notice a dimly lit light in the background. ')
        elif part == 1.3:
            print('You lay there,   gasp   ,  thinking...thinking....thinking...')
            self.agony(5)
        elif part == 2.1:
            print('You scream, and jump out of the wagon. You land harshly on a dirt trail. ')
        elif part == 2.2:
            print('You burst awake, not making a peep, you start obserbing your surroundings. ')
        elif part == 2.3:
            print('You wake up and slowly sit up, unaware of whats happening. Your trying to process it all. ')
        elif part == 3.1:
            print('Look around.')
        elif part == 3.2:
            print('Your walking around. Unsure what to do next. ')
        elif part == 3.3:
            print('You sit there in silence. A door bursts open and footsteps fill the silence. ')

#time.sleep(1)

class Game(Initialize):
    def __init__(self):
        self.gamestart()
    
    def gamestart(self):
        # Starting the journey
        phrase = Initialize.getphrases()
        print(phrase[0])
        Player.level += 1
        Initialize.option(phrase[1], phrase[2], phrase[3])
        choice = int(input('\nWhat is your choice? '))
        if phrase[4] == 1:
            if choice == 1:
                Initialize.story(self, 1.1)
                Initialize.option('Get quite and hide.', 'Stay somewhat still and observe ', 'Start yelling at them to help you.')
                choice = int(input('Whats your choice? ')) 
                if choice == 1:
                    print("You get quite and hide. Unsure what to do next.")
                elif choice == 2:
                    print("You jerk towards the voices. They are saying something about the 'expiriment'?")
                elif choice == 3:
                    print("3")
            elif choice == 2:
                Initialize.story(1.2)
            elif choice == 3:
                Initialize.story(self, 1.3)
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
