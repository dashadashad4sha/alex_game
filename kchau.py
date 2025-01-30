import pygame
import random

pygame.init()


class MainCar:
    def __init__(self):
        self.a = 0

    color = 'white'
    car_rect = pygame.rect.Rect((0, 0, 50, 100))
    car_rect.center = (250, 330)
    speed = 5

    def blit_car(self, d):
        pygame.draw.rect(d, self.color, self.car_rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.car_rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.car_rect.x += self.speed

    def is_glitch(self, stone):
        if self.car_rect.colliderect(stone.stone_rect):
            return True
        return False

    def glitch(self):
        if self.a % 2 == 1:
            self.car_rect.x -= 3

        elif self.a % 2 == 0:
            self.car_rect.x += 3

        self.a += 1


class Bibiki:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.bibiki = pygame.Rect((0, 0, 50, 100))
        self.bibiki.midbottom = (random.randint(0, 500), 0)
        self.a = 0

    speed = 4

    def move(self):
        self.bibiki.y += self.speed

    def blit_bibika(self, d):
        pygame.draw.rect(d, self.color, self.bibiki)

    def is_glitch(self, stone):
        if self.bibiki.colliderect(stone.stone_rect):
            return True
        return False

    def glitch(self):
        if self.a % 2 == 1:
            self.bibiki.x -= 3

        elif self.a % 2 == 0:
            self.bibiki.x += 3

        self.a += 1

class Stone:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        a = random.randint(20, 35)
        self.stone_rect = pygame.Rect((0, 0, a, a))
        self.stone_rect.midbottom = (random.randint(0, 500), 0)

    speed = 2

    def blit_stone(self, d):
        pygame.draw.rect(d, self.color, self.stone_rect)

    def move(self):
        self.stone_rect.y += self.speed


display = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

# bibiki_logic = Bibiki()
car_logic = MainCar()
bibiki = []

stones = []

time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill('pink')

    car_logic.blit_car(display)
    car_logic.move()

    if time % 50 == 0:
        bibiki.append(Bibiki())
        print(bibiki)

    for car in bibiki:
        car.blit_bibika(display)
        car.move()
        if car.bibiki.top > 410:
            bibiki.remove(car)

    if time % 100 == 10:
        stones.append(Stone())

    for st in stones:
        st.blit_stone(display)
        st.move()
        if st.stone_rect.top > 410:
            stones.remove(st)

        if car_logic.is_glitch(st):
            car_logic.glitch()

    for car in bibiki:
        for st in stones:
            if car.is_glitch(st):
                car.glitch()


    time += 1
    pygame.display.update()
    clock.tick(80)
