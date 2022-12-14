""" This is a skeleton of future module 3 task."""
from random import randint

ENEMY_HEALTH_LEVEL = 5
PLAYER_HEALTH_LEVEL = 5
PLAYER_SCORE = 0
print("Starting game..."
      "Attack enemy, chose your weapon:\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n")

while True:
    user_attack = int(input("\nPlease enter your attack:"
                            "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
    ENEMY_DEFENCE = int(randint(1, 3))
    print(f"Enemy defence... {ENEMY_DEFENCE}")
    if user_attack == 1:
        if ENEMY_DEFENCE == 1:
            print("IT'S A DRAW!")
        elif ENEMY_DEFENCE == 2:
            print("YOUR ATTACK IS SUCCESSFUL!")
            ENEMY_HEALTH_LEVEL -= 1
            PLAYER_SCORE += 1
        elif ENEMY_DEFENCE == 3:
            print("YOUR ATTACK IS FAILED!")

    if user_attack == 2:
        if ENEMY_DEFENCE == 1:
            print("YOUR ATTACK IS FAILED!")
        elif ENEMY_DEFENCE == 2:
            print("IT'S A DRAW!")
        elif ENEMY_DEFENCE == 3:
            print("YOUR ATTACK IS SUCCESSFUL!")
            ENEMY_HEALTH_LEVEL -= 1
            PLAYER_SCORE += 1

    if user_attack == 3:
        if ENEMY_DEFENCE == 1:
            print("YOUR ATTACK IS SUCCESSFUL!")
            ENEMY_HEALTH_LEVEL -= 1
            PLAYER_SCORE += 1
        elif ENEMY_DEFENCE == 2:
            print("YOUR ATTACK IS FAILED!")
        elif ENEMY_DEFENCE == 3:
            print("IT'S A DRAW!")

    user_defence = int(input("\nPlease enter your defence:"
                             "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
    ENEMY_ATTACK = int(randint(1, 3))
    print(f"Enemy attack... {ENEMY_DEFENCE}")
    if ENEMY_ATTACK == 1:
        if user_defence == 1:
            print("IT'S A DRAW!")
        elif user_defence == 2:
            print("YOUR DEFENCE IS FAILED!")
            PLAYER_HEALTH_LEVEL -= 1
        elif user_defence == 3:
            print("YOUR DEFENCE IS SUCCESSFUL!")

    if ENEMY_ATTACK == 2:
        if user_defence == 1:
            print("YOUR DEFENCE IS SUCCESSFUL!")
        elif user_defence == 2:
            print("IT'S A DRAW!")
        elif user_defence == 3:
            print("YOUR DEFENCE IS FAILED!")
            PLAYER_HEALTH_LEVEL -= 1

    if ENEMY_ATTACK == 3:
        if ENEMY_DEFENCE == 1:
            print("YOUR DEFENCE IS FAILED!")
            PLAYER_HEALTH_LEVEL -= 1
        elif ENEMY_DEFENCE == 2:
            print("YOUR DEFENCE IS SUCCESSFUL!")
        elif ENEMY_DEFENCE == 3:
            print("IT'S A DRAW!")

    print(f'{ENEMY_HEALTH_LEVEL = }\n')
    if ENEMY_HEALTH_LEVEL <= 0:
        PLAYER_SCORE += 5
        print(f'{PLAYER_SCORE = }')
        print('Game over')
        break
    if PLAYER_HEALTH_LEVEL <= 0:
        print(f'{PLAYER_SCORE = }')
        print('Game over')
        break
