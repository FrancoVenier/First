
poke_select = input("Choose your opponent (Squirtle / Charmander / Bulbasour): ") .upper()

pikachu_life = 100
enemy_life = 0

if poke_select == "SQUIRTLE":
    enemy_life = 90
    print("You will fight against Squirtle!!")
elif poke_select == "CHARMANDER":
    enemy_life = 85
    print("You will fight against Charmander!!")
elif poke_select == "BULBASOUR":
    enemy_life = 100
    print("You will fight against Bulbasour!!")

while pikachu_life > 0 and enemy_life > 0:
    choose_attack = input("Select Pikachu Attacks (Impactrueno / Light Attack)") .upper()

    if choose_attack == "IMPACTRUENO":
        print("PikaPikaCHUUUUUUUUU!!!!")
        enemy_life -= 15
    elif choose_attack == "LIGHT ATTACK":
        print("that was very easy, wasn't it ?")
        enemy_life -= 8

    print("The enemy has {} points of life".format(enemy_life))

    if poke_select == "SQUIRTLE":
        print("Squirtle attacks Pikachu quickly and does 9 damage")
        pikachu_life -= 9
    elif poke_select == "CHARMANDER":
        print("Charmander sets Pikachu on fire and does 11 damage")
        pikachu_life -= 11
    elif poke_select == "BULBASOUR":
        print("Bulbasour gave Pikachu a hug and does 7 damage")
        pikachu_life -= 7

    print("The ¨PikaPika life is {} life points".format(pikachu_life))

if enemy_life <= 0:
    print("Congrats!!! You win the fight!!!")

if pikachu_life <= 0:
    print("Oohh its a shame you lost this fight, good luck for the next Poke fight!")

print("The fight is over")