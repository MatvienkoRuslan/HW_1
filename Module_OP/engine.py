""" Let's fight begin """
from exceptions import EnemyDown, GameOver
from models import Enemy, Player
from settings import ENEMY_HEALTH_LEVEL


def get_player_name():
    """ take name for player """
    player = input('Please enter your name: ')
    return player


def play() -> None:
    """ play the game """
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy(ENEMY_HEALTH_LEVEL)
    score_list = []
    print(f'{ENEMY_HEALTH_LEVEL = }')
    flag = True
    just_do_it = input('AVAILABLE MENU CHOICES: PLAY, SCORES, EXIT\n'
                       'TYPE YOUR CHOICE HERE: ')
    if just_do_it == 'PLAY':
        while flag:
            try:
                player.attack(enemy)
                player.defence(enemy)
            except EnemyDown:
                player.score += 5
                print(f'You WIN! \n Your score: {player.score}')
                score_list.append(player.name)
                score_list.append(player.score)
                with open("file_with_score.txt", "a") as file:
                    print(*score_list, file=file, sep=' \n')
                enemy = Enemy(ENEMY_HEALTH_LEVEL + 1)
            except GameOver:
                print(f'GAME OVER! \n Enemy level: {enemy.level} \n Your score: {player.score}')
                score_list.append(player.name)
                score_list.append(player.score)
                flag = False
            except KeyboardInterrupt:
                print(f'Enemy level: {enemy.level} \n Your score: {player.score}')
                break
    elif just_do_it == 'SCORES':
        score_file = open("file_with_score.txt", "r")
        print(score_file.read())
        play()
    elif just_do_it == 'EXIT':
        flag = False


if __name__ == '__main__':
    play()
