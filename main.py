import pygame

from finaal import FinalScene
from first_scene import FirstScene
from gonki import Races
from labirint import Labirint
from second_scene import SecondScene
from bird import Bird
from third_scene import ThirdScene

pygame.init()


def main():
    games = [
        FirstScene(),
        Labirint(),
        SecondScene(),
        Bird(),
        ThirdScene(),
        Races(),
        FinalScene(),
    ]
    current_game_index = 0

    while current_game_index < len(games):
        games[current_game_index].is_running = True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_u:
                    current_game_index += 1
        current_game = games[current_game_index]
        current_game.run()

        current_game_index += 1


main()
