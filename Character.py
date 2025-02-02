class Character:
    LVL_UP_CONST = 20
    #const for lvl_up
    def __init__(self, name, lvl =1 ,experience = 0 , hp = 1000,mana= 120, dd= 100):
        self.name = name
        self.lvl = 1
        self.experience = 0
        self.hp = 1000
        self.mana = 120
        self.dd = 100
        if isinstance(self,Druid):
            self.mana_moon = 120  # stat only dru = mana moon
        if isinstance(self,Mag):
            self.mana_sun = 120



    def lvl_up(self, num):
        if self.experience >= self.lvl * num:
            self.lvl += 1
            self.experience = 0
            print(f"{self.name} получил новый {self.lvl} уровень")

    def auto_attack(self,character):
        if self.hp >= 0:
            character.hp -= self.dd
            self.experience += 10
            print(character.name, "получил урон, и осталось хп = ", character.hp)
            self.lvl_up(self.LVL_UP_CONST)

    # lvl_up -> we turn experience into lvl while lowering experience to 0


class Druid(Character):

    #skill druid damage moon
    def moon_damage(self, character):
        if self.hp >= 0:
            if self.mana >= 20:
                character.hp -= self.mana_moon
                self.experience += 50
                self.mana -= 20
                print(character.name, "получил лунный урон, и осталось хп = ", character.hp)


class Mag(Character):
    # skill druid damage moon
    def sun_damage(self, character):
        if self.hp >= 0:
            if self.mana >=20:
                character.hp -= self.mana_sun
                self.experience += 50
                self.mana -=20
                print(character.name, "получил солнечный урон, и осталось хп = ", character.hp)