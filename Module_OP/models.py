"""
 Model of players and enemy's

"""
from random import randint

import settings
from exceptions import EnemyDown, GameOver


class Enemy:
    """ Create a new enemy  """

    def __init__(self, level: int):
        self.level = level

    def __str__(self):
        return f'{self.level = }'

    def decrease_health(self):
        """ decrease health """
        self.health_point -= 1
        if self.health_point < 1:
            raise EnemyDown
        return self.health_point

    def select_attack(self):
        """ enemy random attack """
        enemy_attack = randint(1, 3)
        return enemy_attack

    def select_defence(self):
        """ enemy random defence """
        enemy_defence = randint(1, 3)
        return enemy_defence


class Player:
    """ Create a new player """

    def __init__(self, name: str, health_point=settings.INITIAL_PLAYER_HEALTH):
        self.name = name
        self.health_point = health_point
        self.score = 0

    def decrease_health(self):
        """ decrease health """
        self.health_point -= 1
        if self.health_point < 1:
            raise GameOver
        return self.health_point

    def select_attack(self):
        """ select attack """
        user_attack = int(input("\nPlease enter your attack:"
                                "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
        return user_attack

    def select_defence(self):
        """ select defence """
        user_defence = int(input("\nPlease enter your defence:"
                                 "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
        return user_defence

    @staticmethod
    def fight(attack, defence):
        """ Mortal Combat"""
        if attack == 1 and defence == 1 or attack == 2 and defence == 2 \
                or attack == 3 and defence == 3:
            return 1
        if attack == 1 and defence == 2 or attack == 2 and defence == 1 \
                or attack == 3 and defence == 2:
            return 2
        if attack == 1 and defence == 3 or attack == 2 and defence == 3 \
                or attack == 3 and defence == 1:
            return 3

    def attack(self, enemy) -> None:
        """Attack"""
        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)
        if fight_result == 1:
            print("IT'S A DRAW!")
        elif fight_result == 2:
            print("YOUR ATTACK IS FAILED!")
            settings.PLAYER_HEALTH_LEVEL -= 1
        elif fight_result == 3:
            enemy.decrease_health()
            self.score += 1
            print("YOUR ATTACK IS SUCCESSFUL!")
            print(f"Enemy have just: {enemy.level}")

    def defence(self, enemy: Enemy) -> None:
        """Defense"""
        attack = enemy.select_attack()
        defence = self.select_defence()
        fight_result = self.fight(attack, defence)
        if fight_result == 1:
            print("IT'S A DRAW!")
        elif fight_result == 2:
            print("YOUR DEFENCE IS FAILED!")
            self.decrease_health()
            print(f"You have just: {self.health_point}")
        elif fight_result == 3:
            print("YOUR DEFENCE IS SUCCESSFUL!")
