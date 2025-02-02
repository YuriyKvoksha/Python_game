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