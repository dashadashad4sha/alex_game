import pygame
import sys
import random

from labirint import Leha
from parent_class import Main

pygame.init()

WIDTH = 500
HEIGHT = 400
ARIAL_30 = pygame.font.SysFont('Arial', 30)


class Car:
    speed = 6
    is_collision = False
    surf = pygame.Surface((90, 124), pygame.SRCALPHA, 32)
    stone_collision = 0

    def __init__(self):
        self.rect = pygame.Rect((random.randint(50, WIDTH - 125), -100, 90, 124))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_color = []
        for c in self.color:
            new_color.append(int(c * 1.3 % 256))
        self.new_color = tuple(new_color)

    def move(self):
        self.rect.y += self.speed

    def blit_car(self, s):
        """
        Отрисовка машин
        :param s: surface, на котором будет машина
        """
        #  wheels
        pygame.draw.rect(self.surf, '#1b1c1c', (0, 0, 20, 30))
        pygame.draw.rect(self.surf, '#1b1c1c', (70, 0, 20, 30))
        pygame.draw.rect(self.surf, '#1b1c1c', (0, 94, 20, 30))
        pygame.draw.rect(self.surf, '#1b1c1c', (70, 94, 20, 30))
        #  kuzov
        pygame.draw.rect(self.surf, self.color, (20, 12, 50, 100))
        pygame.draw.rect(self.surf, self.new_color, (24, 22, 42, 55))
        #  lights
        pygame.draw.rect(self.surf, 'yellow', (24, 100, 14, 7))
        pygame.draw.rect(self.surf, 'yellow', (52, 100, 14, 7))
        #  tubes
        pygame.draw.rect(self.surf, 'gray', (25, 4, 5, 8))
        pygame.draw.rect(self.surf, 'gray', (60, 4, 5, 8))

        s.blit(self.surf, self.rect)

    def collision_animation(self, main_car):
        """
        Анимация столкновения с машиной
        :param main_car: объект класса машины пользователя
        """
        if self.is_collision:
            if main_car.rect.left > self.rect.left:
                self.rect.x -= 7
            else:
                self.rect.x += 7
            self.speed += 1

    def stone_collision_method(self, stone_obj):
        if self.rect.colliderect(stone_obj.rect) and self.stone_collision == 0:
            self.stone_collision = 10

    def stone_collision_animation(self):
        if self.stone_collision > 0:
            if self.stone_collision % 8 <= 4:
                self.rect.x += 4
            else:
                self.rect.x -= 4
            self.stone_collision -= 1


class MainCar:
    rect = pygame.Rect(0, 0, 80, 120)
    rect.midbottom = (WIDTH // 2, HEIGHT - 40)
    speed = 7
    stone_collision = 0

    surf = pygame.Surface((80, 120), pygame.SRCALPHA, 32)

    lives = 3

    sound_collapse = pygame.mixer.Sound('sounds_and_music/sounds/races_collapse.wav')

    def blit_car(self, s):
        # kuzov
        pygame.draw.rect(self.surf, '#f3d0f4', (15, 10, 50, 100))
        pygame.draw.rect(self.surf, '#fdd9af', (20, 35, 40, 70))
        # wheels
        pygame.draw.rect(self.surf, '#000000', (0, 0, 15, 25))
        pygame.draw.rect(self.surf, '#000000', (65, 0, 15, 25))
        pygame.draw.rect(self.surf, '#000000', (0, 95, 15, 25))
        pygame.draw.rect(self.surf, '#000000', (65, 95, 15, 25))
        # light
        pygame.draw.rect(self.surf, '#fffa1d', (22, 5, 14, 7))
        pygame.draw.rect(self.surf, '#fffa1d', (44, 5, 14, 7))

        # lives
        x = 20
        for i in range(0, self.lives):
            pygame.draw.circle(s, 'red', (x, 20), 5)
            x += 20

        # car
        s.blit(self.surf, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.stone_collision > 0:
            self.stone_collision -= 1
            if keys[pygame.K_d] and self.rect.right <= WIDTH:
                self.rect.x += 1
            if keys[pygame.K_a] and self.rect.left >= 0:
                self.rect.x -= 1
        else:
            if keys[pygame.K_d] and self.rect.right <= WIDTH:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.left >= 0:
                self.rect.x -= self.speed

    def collisions(self, obj):
        if self.rect.colliderect(obj.rect) and not obj.is_collision:
            self.lives -= 1
            obj.is_collision = True
            self.sound_collapse.play()

    def restart_coords(self):
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 40)


class Stone:
    speed = 3
    sound_stone = pygame.mixer.Sound('sounds_and_music/sounds/races_stone.wav')
    sound_stone.set_volume(0.2)

    def __init__(self):
        width = random.randint(10, 50)
        self.rect = pygame.Rect((random.randint(0, WIDTH), 0, width, width))
        self.rect.bottom = 0
        n = random.randint(0, 235)
        self.color = (n, n, n)

    def blit_stone(self, s):
        pygame.draw.rect(s, self.color, self.rect)

    def move_stone(self):
        self.rect.y += self.speed

    def collision_animation(self, main_car):
        """
        Анимация столкновения с камнем
        :param main_car: объект класса машины пользователя
        """
        if self.rect.colliderect(main_car.rect):
            main_car.stone_collision = 20
        if main_car.stone_collision == 20:
            self.sound_stone.play()


class Races(Main):
    lesha_logic = Leha(None, None)
    replace_leha_center_flag = True

    car_first_object = Car()
    cars = [car_first_object]

    stone_first_object = Stone()
    stones = [stone_first_object]

    timer = 0

    main = MainCar()

    filarmonia_rect = pygame.Rect((0, 0, 400, 400))
    filarmonia_rect.midbottom = (250, 0)

    def run(self):

        music_races = pygame.mixer.Sound('sounds_and_music/music/interworld-metamorphosis_(trmuz.net).mp3')
        music_races.set_volume(0.15)
        music_races.play()
        while self.is_running:
            self.display.fill('#CFCFDD')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.main.lives == 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.main.lives = 3
                            self.cars = []
                            self.stones = []
                            self.main.restart_coords()
                            self.timer = 0

            if self.main.lives > 0 and self.timer < 2000:
                #  STONES LOGIC
                if self.timer % 73 == 0:
                    new_stone = Stone()
                    self.stones.append(new_stone)

                for stone in self.stones:
                    stone.blit_stone(self.display)
                    stone.move_stone()
                    stone.collision_animation(self.main)

                for stone in self.stones:  # remove stones
                    if stone.rect.top > HEIGHT:
                        self.stones.remove(stone)

                #  CARS LOGIC
                self.timer += 1
                if self.timer % 60 == 0:  # spawn new cars
                    new_car = Car()
                    self.cars.append(new_car)

                for car in self.cars:  # show cars
                    car.blit_car(self.display)
                    car.move()
                    car.collision_animation(self.main)
                    for stone in self.stones:
                        car.stone_collision_method(stone)
                    car.stone_collision_animation()

                for car in self.cars:  # remove cars
                    if car.rect.top > HEIGHT or car.rect.left > WIDTH or car.rect.right < 0:
                        self.cars.remove(car)

                #  USER LOGIC
                self.main.blit_car(self.display)
                self.main.move()
                for car in self.cars:
                    self.main.collisions(car)

                timer_text = ARIAL_30.render(f'{self.timer // 20}', True, 'black')
                self.display.blit(timer_text, (WIDTH - 50, 10))

            elif self.main.lives <= 0 and self.timer < 2000:
                self.display.fill("#f5e9c9")
                self.display_window("no", "Нажмите Enter")
            elif self.timer >= 2000:
                timer_text = ARIAL_30.render(f'{self.timer // 20}', True, 'black')
                self.display.blit(timer_text, (WIDTH - 50, 10))

                self.display.blit(self.filarmonia, self.filarmonia_rect)
                self.filarmonia_rect.y += 1
                if self.filarmonia_rect.bottom >= 350:
                    music_races.stop()
                    self.is_running = False

                if not self.main.rect.colliderect(self.filarmonia_rect):
                    self.main.blit_car(self.display)
                    self.main.move()
                    for car in self.cars:
                        self.main.collisions(car)
                else:
                    if self.replace_leha_center_flag:
                        self.replace_leha_center_flag = False
                        self.lesha_logic.leha_rect.center = self.main.rect.center
                    self.lesha_logic.leha_move()
                    self.lesha_logic.blit_lesha()

            # COMMON SETTINGS
            pygame.display.update()
            self.clock.tick(60)
