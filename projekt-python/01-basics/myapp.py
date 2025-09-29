

class Skill:
    def __init__(self, name, cost, power, skill_type):
        self.name = name
        self.cost = cost
        self.skill_type = skill_type
        self.power = power


class Creature:
    def __init__(self, isPlayer, maxHP, Armor, maxMana, damage, lvl):
        self.isPlayer = isPlayer
        self.HP = maxHP
        self.maxHP = maxHP
        self.Armor = Armor
        self.maxMana = maxMana
        self.Mana = maxMana
        self.damage = damage
        self.lvl = lvl

skills = [
    Skill("minor restoration", 0, 3, "manaGain"),
    Skill("minor heal", 3, 5, "heal"),
    Skill("fireball", 2, 4, "damage"),
    Skill("shield", 1, 3, "defense")
]

enemies = [
    Creature(False, 5, 0, 3, 2, 1),
    Creature(False, 7, 0, 5, 2, 2),
    Creature(False, 10, 0, 3, 2, 3),
    Creature(False, 8, 0, 5, 3, 4),
    Creature(False, 12, 0, 5, 3, 5),
    Creature(False, 15, 0, 6, 4, 6),

]

game_over = False
blocking = False
global lvl
lvl = 0
player = Creature(True, 10, 0, 5, 3, 1)
action_menu = "1 - attack       2 - cast        3 - block"
action = 0
player_image = ("  _  \n"
                " | | \n"
                " _-_ \n"
                "/ | \\\n"
                "| | |\n"
                " / \\\n"
                "/   \\   \n \n")

monster_image = ("   _____   \n"
                 "  / . . \\  \n"
                 " /   |   \\  \n"
                 " \\  _--_ /  \n"
                 "  \\_____/\n \n \n")

def spell_menu ():
    skill_casted = 5
    for i in range (4):
        print ("Press %d for %s - COST:%d mana, %s %d  \n"%(i+1, skills[i].name, skills[i].cost, skills[i].skill_type, skills[i].power))
    skill_casted = int(input(" ### Enter 1 - 4 numbber ### \n"))-1
    print ("You have casted a %s spell \n"%(skills[skill_casted].name))
    if skill_casted == 0:
        if player.Mana <= player.maxMana - skills[skill_casted].power:
            player.Mana += skills[skill_casted].power
        else:
            player.Mana = player.maxMana


    elif skill_casted == 1:
        if player.HP <= player.maxHP - skills[skill_casted].power:
            player.HP += skills[skill_casted].power
        else:
            player.HP = player.maxHP

    elif skill_casted == 2:
        enemies[lvl].HP -= skills[skill_casted].power
    elif skill_casted == 3:
        player.Armor += skills[skill_casted].power

    player.Mana -= skills[skill_casted].cost
    if player.Mana < 0:
        player.HP += player.Mana * 2
        print("You take damage from exaustion, try to regain mana. \n")
        player.Mana = 0

def enemy_turn (lvl, blocking):
    if enemies[lvl].HP <= 0:
        lvl += 1
    else:
        if blocking == False:
            player.Armor -= enemies[lvl].damage
        else:
            player.Armor -= 1
    if player.Armor <= 0:
        player.HP += player.Armor
        player.Armor = 0
    player.Mana += 1
    if player.HP <= 0:
        game_over = True




while not game_over:
    print("HP: %d/%d    Armor: %d    Mana: %d/%d" %(enemies[lvl].HP, enemies[lvl].maxHP, enemies[lvl].Armor, enemies[lvl].Mana, enemies[lvl].maxMana))
    print(monster_image)
    print("HP: %d/%d    Armor: %d    Mana: %d/%d" %(player.HP, player.maxHP, player.Armor, player.Mana, player.maxMana))
    print(player_image)
    print(action_menu)
    print(lvl)

    action = int(input("Enter 1 - 3 numbber \n"))

    if action == 1:
        enemies[lvl].HP -= player.damage
    elif action == 2:
        spell_menu()
    elif action == 3:
        blocking = True


    enemy_turn(lvl, blocking)
    blocking = False


print("Game Over")


