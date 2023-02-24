# Player file for instantiating the player.

class Player:
    def __init__(self, currentHP=50, maxHP=100, gold=1, exp=1, level=1, strength=0, agility=0, dexterity=1, armor=1, blessing=0, CurrentStory=1, isChained=True):
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.gold = gold
        self.exp = exp
        self.level = level
        self.strength = strength
        self.agility = agility
        self.dexterity = dexterity
        self.armor = armor
        self.blessing = blessing
        self.isChained = isChained
        self.CurrentStory = CurrentStory

    def loadPlayer(self):
        with open("./save/save.txt") as saveFile:
            lines = [line.rstrip() for line in saveFile]

            self.currentHP = int(lines[0])
            self.maxHP = int(lines[1])
            self.gold = int(lines[2])
            self.exp = int(lines[3])
            self.level = int(lines[4])
            self.strength = int(lines[5])
            self.agility = int(lines[6])
            self.dexterity = int(lines[7])
            self.armor = int(lines[8])
            self.blessing = int(lines[9])
            self.isChained = bool(lines[11])
            self.CurrentStory = int(lines[10])

            print("Save Found, importing data.")

    def createPlayer(self):
        file = open("./save/save.txt", "x")
        file.close()
        self.currentHP = 50
        self.maxHP = 100
        self.gold = 1
        self.exp = 1
        self.level = 1
        self.strength = 0
        self.agility = 0
        self.dexterity = 1
        self.armor = 1
        self.blessing = 0
        self.CurrentStory = 1
        self.isChained = True
        print("No Save, creating new one.")
    
    def savePlayer(self):
        with open("./save/save.txt", "w") as saveFile:
            saveFile.write(str(self.currentHP) + "\n")
            saveFile.write(str(self.maxHP) + "\n")
            saveFile.write(str(self.gold) + "\n")
            saveFile.write(str(self.exp) + "\n")
            saveFile.write(str(self.level) + "\n")
            saveFile.write(str(self.strength) + "\n")
            saveFile.write(str(self.agility) + "\n")
            saveFile.write(str(self.dexterity) + "\n")
            saveFile.write(str(self.armor) + "\n")
            saveFile.write(str(self.blessing) + "\n")
            saveFile.write(str(self.CurrentStory) + "\n")
            saveFile.write(str(int(self.isChained)) + "\n")
