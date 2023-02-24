from os.path import exists
from player import Player
from commands import Commands
from storyText import mainStory, lookStory
import sys

currentLevel = 1
CurrentStory = 1
NextLevelCheck = False

def gameInit():
    global player
    player = Player()
    if exists("./save/save.txt"):
        player.loadPlayer()

    else:
        # Add the save file creation when the player saves, possibly or autosave.
        player.createPlayer()

def storyBreak():
    global player
    print("\nEnter a command. Type 'help' for a list of all available commands. >> ",end="")
    choice = input()
    
    if choice == "help":
        Commands.Help()
        storyBreak()
    
    elif choice == "stats":
        Commands.Stats(player)
        storyBreak()
    
    elif choice == "save":
        saveOrNo = input("\nWould you like to save and quit? (y/n) >> ")
        if saveOrNo == "y":
            player.savePlayer()
            sys.exit()
        else:
            storyBreak()
    elif choice == "look":
        lookStory(CurrentStory)
        storyBreak()
    
    else:
        print("Unknown command, please make sure you are spelling it right.")
        storyBreak()

def main():
    # Main method that runs the whole thing.

    print("Welcome to Heaven's Fall")

    gameInit()

    print("Press <Enter> to continue >> ",end="")
    input()

    for _ in range(1, CurrentStory + 1):
        mainStory(CurrentStory)
        storyBreak()
    
    print("The program ran successfully")

if __name__ == "__main__":
    main()
