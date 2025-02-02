from Character import *
if __name__ == '__main__':
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

        print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
