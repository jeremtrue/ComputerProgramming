import random as rand



class Monster:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.damage = 0
        self.coins = 0
        self.spareResistance = 0

    def RandomizeStats(self):
        names = ['ork the stork', 'goof the toof', 'slime the kime', 'mr electorium on that beat', 'spider the kiter']
        self.name = rand.choice(names)
        self.health = rand.randint(50, 100)  # You can set the health range as needed
        self.damage = rand.randint(5, 20)    # You can set the damage range as needed
        self.coins = rand.randint(1, 10)     # You can set the coin range as needed
        self.spareResistance = round(rand.uniform(0.3, 0.9), 2)
        print("monsters spare resistance", self.spareResistance)

    def TakeDamage(self, damage):
        self.health -= damage
        print("Enemy was hit!")
    
    def Death(self, player):
        player.coins =+ self.coins

    def Spare(self):
        successBool = False
        playerChance = 0.1
        roll = playerChance * round(rand.uniform(1, 9,), 2)
        if roll > self.spareResistance:
            successBool = True
            return successBool
        
class SwordTemplate:
        def __init__(self, name, damageRange, description):
            self.name = name
            self.damageRange = damageRange
            self.description = description

class Player:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.damage = 0
        self.coins = 0
        self.sparedEnemies = 0

    def TakeDamage(self, damage):
        self.health -= damage

    def Death(self, Game):
        Game.InstializePlayer()

class MainGame:
    ironsword = SwordTemplate("Iron Sword", 10, "Common adventurer sword")
    woodensword = SwordTemplate("Wooden Sword", 2, "This should just be classified as a stick")
    obsidiansword = SwordTemplate("Obsidian Sword", 15, "Very sharp edges cut through mobs")
    flamesword = SwordTemplate("Flame Sword", 20, "Combusts using the gel of slimes")
    excalibersword = SwordTemplate("Excaliber", 2, "Ancient sword found in a large rock")
     
    def __init__(self):
        self.levelCount = 0
        self.enemy = ""
        self.woodensword
        self.ironsword
        self.obsidiansword
        self.flamesword
        self.excalibersword

    def InitializePlayer(player):
        player = Player()
        player.name = input("Enter Name: ")
        player.health = int(input("Enter Health: "))
        player.damage = int(input("Enter Damage: "))
        return player

    def MainGameFunc(player, Game):
        # create a new enemy
        monster = Monster()
        monster.RandomizeStats()

        # main game loop
        if monster.health >= 0:
            print("--------------------------------------")
            print('|', player.name)
            print('| Health:', player.health)
            print('| Damage:', player.damage)
            print('| Spared enemies', player.sparedEnemies)
            print('|')
            print('|')
            print('|')
            print('| Monster:', monster.name)
            print('| Health:', monster.health)
            print('| Damage:', monster.damage)
            print("--------------------------------------")
            
            # get the action input from the character
            match str(input('Attack | Spare: ')).lower():
                case "attack":
                    # monster takes damage
                    monster.TakeDamage(player.damage)
                    print(player.name, "took", monster.damage, "damage")
                    #if monster is still alive, you take damage
                    if monster.health > 0:
                        player.TakeDamage(monster.damage)
                        print(monster.name, "took", player.damage, "damage")
                ############################################################
                # spare a monster
                case "spare":
                    print("attempted spare!")
                    
                    if monster.Spare():
                        print("monster Spared!")
                        player.sparedEnemies += 1
                        
                    print("spare failed")
                    player.TakeDamage(monster.damage)
                    print(player.name, "took", monster.damage, "damage")
                ############################################################
        elif player.health <= 0:
            {
                player.Death()
            }
        else:
            {
                print("next fight!")
                # Game.MainGameFunc(player, Game)
            }
        



