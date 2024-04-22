import pygame
import random

pygame.init()

display = pygame.display.set_mode((500, 400))
pygame.display.set_caption('DD GAME')
clock = pygame.time.Clock()

sound1 = pygame.mixer.Sound('sounds_and_music/Jump3.wav')
sound2 = pygame.mixer.Sound('sounds_and_music/Explosion.wav')
pygame.mixer.music.set_volume(0.2)

SPEED = 2
GRAVITY = 1
SCORE = 5

SHRIFT = pygame.font.SysFont('arial', 36)

lhbrd = pygame.Rect((80, 178, 34, 45))

offset = 0
gap = 140
walltop = pygame.Rect((300, 0-offset, 100, 200))
wallbottom = pygame.Rect((300, 200-offset+gap, 100, 200))

jump_time = 0
jump_force = 0
gravity_force = 1

meteor_wall_bottom = pygame.image.load('img/meteor_wall.png')
meteor_wall_bottom = pygame.transform.scale(meteor_wall_bottom, (100, 200))

meteor_wall_top = pygame.image.load('img/meteor_wall.png')
meteor_wall_top = pygame.transform.flip(meteor_wall_top, 1, 1)
meteor_wall_top = pygame.transform.scale(meteor_wall_top, (100, 200))

leha__img = pygame.image.load('img/leha_jatpak.png')
leha__img = pygame.transform.scale(leha__img, (34, 45))

background = pygame.image.load('img/sky.jpg')
background = pygame.transform.scale(background, (500, 400))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
            jump_time += 20
            jump_force += 8
            sound1.play()

    if SCORE > 0:
        display.blit(background, (0, 0))

        display.blit(leha__img, lhbrd)
        display.blit(meteor_wall_bottom, wallbottom)
        display.blit(meteor_wall_top, walltop)

        walltop.x -= SPEED
        wallbottom.x -= SPEED

        score_text = SHRIFT.render(f'{5 - SCORE}', True, 'white')
        display.blit(score_text, (10, 10))

        if lhbrd.top > 400:
            lhbrd.bottom = 0
            gravity_force = 1

        if jump_time > 0:
            lhbrd.y -= jump_force
            if jump_force > 1:
                jump_force -= 1
            jump_time -= 1
            if jump_time == 0:
                gravity_force = 1
        else:
            gravity_force += 0.2
            lhbrd.y += gravity_force

        if walltop.right < 0:
            offset = random.randint(0, 100)
            gap = 140

            walltop = pygame.Rect((500, 0 - offset, 100, 200))
            wallbottom = pygame.Rect((500, 200 - offset + gap, 100, 200))
            SCORE -= 1

        if walltop.colliderect(lhbrd) or wallbottom.colliderect(lhbrd):
            sound2.play()
            lhbrd = pygame.Rect((80, 178, 34, 45))
            walltop = pygame.Rect((600, 0 - offset, 100, 200))
            wallbottom = pygame.Rect((600, 200 - offset + gap, 100, 200))
            SCORE = 5
    else:
        display.fill("#04548c")

    pygame.display.update()
    clock.tick(110)

