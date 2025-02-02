# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Character:
    def __init__(self, name, lvl, hp,mana, dd):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mana = mana
        self.dd = dd
    def fight(self,character, hp):
        character.hp -= self.dd
        print(character.name, "fight hp = ", character.hp)
class Druid(Character):
        def __init__(self, manaMoon):
            self.manaMoon = manaMoon #mana moon
        def moon_domage(self, character):
            character.hp -= self.manaMoon
            print(character.name, "moon domage hp = ", character.hp)

class Mag(Character):
    def __init__(self, manaSun):
        self.manaSun = manaSun
    def sun_damage(self, character):
        character.hp -= self.manaSun
        print(character.hp) #ghfhgf
Splitnight = Mag(200)
Splitnight.name = "Splitnight"
Splitnight.hp = 3300
Splitnight.lvl = 26
Splitnight.mana = 130
Splitnight.dd = 600
print(Splitnight.name)
Lonellyday = Druid(300)
Lonellyday.name = "Lonelyday"
Lonellyday.hp = 5500
Lonellyday.lvl = 32
Lonellyday.mana = 120
Lonellyday.dd = 900
Lonellyday.fight(Splitnight, Splitnight.hp)
Lonellyday.moon_domage(Splitnight)
print(Lonellyday.name)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
