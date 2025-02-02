from Character import *

#def druid_creation(character_name):
 #   druid  = Druid(character_name)
  #  print("Druid created sucseful!")

       # f'World hello , {druid.lvl}lvl {druid.experience}exp  {druid.hp}hp, {druid.mana}mana, {druid.dd}dd {druid.manaMoon}manaMoon '


if __name__ == '__main__':
    is_alive = True
    druid_name = input("Input druid name ")
    druid = Druid(druid_name)

    # mag_name = input("Input mag name ")
    mag_name = "Splitnight"
    mag = Mag(mag_name)
    print(f'World hello druid {druid.name}! {druid.lvl}lvl {druid.experience}exp  {druid.hp}hp, {druid.mana}mana, {druid.dd}dd {druid.mana_moon}mana_moon ')
    print(f'World hello mag {mag.name}! {mag.lvl}lvl {mag.experience}exp  {mag.hp}hp, {mag.mana}mana, {mag.dd}dd {mag.mana_sun}mana_sun ')
    def displey_info(character):
        print(f'World hello mag {character.name}! {character.lvl}lvl {character.experience}exp  {character.hp}hp, {character.mana}mana, {character.dd}dd ')

    while is_alive:
        if mag.hp <=0 or druid.hp <=0:
            is_alive = False

        druid.auto_attack(mag)
        mag.auto_attack(druid)
        druid.moon_damage(mag)
        mag.sun_damage(druid)

    print(f'World hello druid {druid.name}! {druid.lvl}lvl {druid.experience}exp  {druid.hp}hp, {druid.mana}mana, {druid.dd}dd {druid.mana_moon}mana_moon ')
    print(f'World hello mag {mag.name}! {mag.lvl}lvl {mag.experience}exp  {mag.hp}hp, {mag.mana}mana, {mag.dd}dd {mag.mana_sun}mana_sun ')
    # Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
