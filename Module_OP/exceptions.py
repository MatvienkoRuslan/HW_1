""" This my exceptions """

class CustomError(Exception):
    """ This base class for all exceptions in this module"""
    pass

class EnemyDown(CustomError):
    """ This class exception where the enemy is down"""

    def __str__(self):
        print('GAME OVER')

class GameOver(CustomError):
    """ This class exception where the game is over and player is dead"""

    def __str__(self):
        print("GAME OVER!")
