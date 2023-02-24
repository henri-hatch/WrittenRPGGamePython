class Commands:
    def Help():
        print("Possible commands are: \n\t 'help' \n\t 'look' \n\t 'stats' \n\t 'interact' \n\t " +
                          "'save' \n\t 'remove' \n\t 'inventory' \n]\t 'remove' \n\t 'use'")
    
    def Stats(player):
        print(f"\nMax HP: {player.maxHP}")
        print(f"\nCurrent HP: {player.currentHP}")
        print(f"\nStrength: {player.strength}")
        print(f"\nDexterity: {player.dexterity}")
        print(f"\nAgility: {player.agility}")
        print(f"\nArmor: {player.armor}")
        print(f"\nBlessing: {player.blessing}")
        print(f"\nGold: {player.gold}")
        print(f"\nCurrent EXP: {player.exp}")
        print(f"\nLevel: {player.level}")
