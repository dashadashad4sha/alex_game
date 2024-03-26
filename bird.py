import pygame
import random

pygame.init()

display = pygame.display.set_mode((500, 400))
pygame.display.set_caption('DD GAME')
clock = pygame.time.Clock()

SPEED = 2
GRAVITY = 1
SCORE = 10

lhbrd = pygame.Rect((80, 178, 34, 45))

offset = 0
gap = 140
walltop = pygame.Rect((300, 0-offset, 100, 200))
wallbottom = pygame.Rect((300, 200-offset+gap, 100, 200))

n = 20
m = 50

is_jump = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
            is_jump = n

    if SCORE > 0:
        display.fill("white")

        pygame.draw.rect(display, 'blue', lhbrd)
        pygame.draw.rect(display, 'green', walltop)
        pygame.draw.rect(display, 'red', wallbottom)

        walltop.x -= SPEED
        wallbottom.x -= SPEED

        if is_jump > 0:
            lhbrd.y -= m/n
            is_jump -= 1
        else:
            lhbrd.y += GRAVITY

        if walltop.right < 0:
            offset = random.randint(0, 100)
            gap = random.randint(110, 140)

            walltop = pygame.Rect((500, 0 - offset, 100, 200))
            wallbottom = pygame.Rect((500, 200 - offset + gap, 100, 200))
            SCORE -= 1

        if walltop.colliderect(lhbrd) or wallbottom.colliderect(lhbrd):
            print("collision")
            lhbrd = pygame.Rect((80, 178, 34, 45))
            walltop = pygame.Rect((600, 0 - offset, 100, 200))
            wallbottom = pygame.Rect((600, 200 - offset + gap, 100, 200))
            SCORE = 10
    else:
        display.fill("#04548c")

    pygame.display.update()
    clock.tick(110)

