from Character import *

if __name__ == '__main__':
    def displey_info(character):
        print(f'Hero  {character.name}! {character.lvl}lvl {character.experience}exp  {character.hp}hp, {character.mana}mana, {character.dd}dd ')
    def dead_detected(characters):

                return False

    druid_name = input("Input druid name ")
    druid = Druid(druid_name)

    # mag_name = input("Input mag name ")
    mag_name = "Splitnight"
    mag = Mag(mag_name)
    print(f'World hello druid {druid.name}! {druid.lvl}lvl {druid.experience}exp  {druid.hp}hp, {druid.mana}mana, {druid.dd}dd {druid.mana_moon}mana_moon ')
    print(f'World hello mag {mag.name}! {mag.lvl}lvl {mag.experience}exp  {mag.hp}hp, {mag.mana}mana, {mag.dd}dd {mag.mana_sun}mana_sun ')

    count_battles = 0# temporarily for counting battles



    while True:
        if druid.hp > 0:
            druid.auto_attack(mag)
        else:
            break
        if mag.hp > 0:
            mag.auto_attack(druid)
        else:
            break
        if druid.hp > 0:
            druid.moon_damage(mag)
        else:
            break
        if mag.hp > 0:
            mag.sun_damage(druid)
        else:
            break
        count_battles += 1
        print(count_battles)

    print(f'World hello druid {druid.name}! {druid.lvl}lvl {druid.experience}exp  {druid.hp}hp, {druid.mana}mana, {druid.dd}dd {druid.mana_moon}mana_moon ')
    print(f'World hello mag {mag.name}! {mag.lvl}lvl {mag.experience}exp  {mag.hp}hp, {mag.mana}mana, {mag.dd}dd {mag.mana_sun}mana_sun ')
    # Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
