import pygame

pygame.init()

pygame.mixer.music.load('sounds_and_music/scene1music.mp3')
pygame.mixer.music.set_volume(0.20)
pygame.mixer.music.play()

display = pygame.display.set_mode((500, 400))
pygame.display.set_caption('DD GAME')
clock = pygame.time.Clock()

background1 = pygame.image.load('img/bg1.png')
background2 = pygame.image.load('img/bg2.png')

window = pygame.image.load('img/plash.png')
windowR = pygame.image.load('img/right.png')
windowL = pygame.image.load('img/left.png')

lesha = pygame.image.load('img/lesha.png')
lesha = pygame.transform.scale(lesha, (200, 400))

alien = pygame.image.load('img/alien.png')
alien = pygame.transform.scale(alien, (200, 400))

font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 12)

scene1_replics = []
f = open('dialogs/scene1.txt', 'r', encoding='utf-8')
for i in range(6):
    scene1_replics.append(f.readline().replace("\n", ""))

i = 0


def display_window(rotation, text):
    if rotation == "l":
        display.blit(windowL, (135, 50))
    elif rotation == "r":
        display.blit(windowR, (135, 50))
    else:
        display.blit(window, (135, 50))

    strings = text.split("=")
    x = 170
    y = 65
    for i in range(0, len(strings)):
        j = i + 1
        y_i = y + 17 * j
        text_surface = font.render(f'{strings[i]}', True, (0, 0, 0))
        display.blit(text_surface, (x, y_i))


def first_scene(i):
    display.fill("#04388c")

    display.blit(lesha, (0, 0))
    display.blit(alien, (320, 0))

    direction = scene1_replics[i][0]

    display_window(direction, scene1_replics[i][1:])


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYDOWN:
            i += 1

    if i < 6:
        first_scene(i)
    else:
        pygame.mixer.music.stop()
        display.fill("#04548c")

    pygame.display.update()
    clock.tick(60)
