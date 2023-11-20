from classes import Game
game = Game()
game.save = Game.Save()
#game.Save.Load
game.Initialize()
if game.save.exists.first == 0:
    def printdir():
        print('How to play:')
        print('First you would enter your name')
        print('Next you would start your journey.')
        print('When you are asked a yes or no questing just type y/n of yes/no.')
        print('When you are asked to input a number from a chart, just type the number next to your asnwer.')
        firstque = input('Do you understand? y/n')
        if firstque == 'y' or firstque == 'yes':
            print('Great! good luck')
        else:
            print('Well then, you see, I have no clue. good luck!')
    printdir()

    
    