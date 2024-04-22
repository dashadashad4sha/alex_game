import pygame
import random

pygame.init()


class MainCar:
    color = 'white'
    car_rect = pygame.rect.Rect((0, 0, 50, 100))
    car_rect.center = (250, 330)

    def blit_car(self):
        pass


display = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill('pink')

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     car_rect.x -= 5
    # if keys[pygame.K_RIGHT]:
    #     car_rect.x += 5
    #
    # pygame.draw.rect(display, 'white', car_rect)

    pygame.display.update()
    clock.tick(80)
