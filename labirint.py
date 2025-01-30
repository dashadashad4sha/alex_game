import pygame
from parent_class import Main


class Coins(Main):
    coins_img = []
    for c in range(1, 6):
        coins_img.append(pygame.transform.scale(pygame.image.load(f"img/coin_animation/ca{c}.png"), (25, 25)))

    coins_rect = [
        pygame.Rect(113, 0, 25, 25),
        pygame.Rect(163, 0, 25, 25),
        pygame.Rect(5, 315, 25, 25),
        pygame.Rect(460, 213, 25, 25)]

    gotten_coins = []  # useless mechanic

    def show_coin(self, coords):
        n = (pygame.time.get_ticks() - 100) % 1500
        display = self.display
        if 0 <= n < 300:
            display.blit(self.coins_img[0], coords)
        elif 300 <= n < 600:
            display.blit(self.coins_img[1], coords)
        elif 600 <= n < 900:
            display.blit(self.coins_img[2], coords)
        elif 900 <= n < 1200:
            display.blit(self.coins_img[3], coords)
        else:
            display.blit(self.coins_img[4], coords)

    def blit_coins(self):
        for coords in self.coins_rect:
            if coords not in self.gotten_coins:
                self.show_coin(coords)


class Walls(Main):
    wall1 = pygame.image.load('img/wall_animation/wall1.png')
    wall1 = pygame.transform.scale(wall1, (100, 10))

    wall2 = pygame.image.load('img/wall_animation/wall2.png')
    wall2 = pygame.transform.scale(wall2, (100, 10))

    wall4 = pygame.image.load('img/wall_animation/wall4.png')
    wall4 = pygame.transform.scale(wall4, (100, 10))

    wall5 = pygame.image.load('img/wall_animation/wall5.png')
    wall5 = pygame.transform.scale(wall5, (100, 10))

    rects_vert = [pygame.Rect(-50, 95, 100, 10),
                  pygame.Rect(-50, 195, 100, 10),
                  pygame.Rect(-50, 295, 100, 10),
                  pygame.Rect(200, 45, 100, 10),
                  pygame.Rect(350, 195, 100, 10),
                  pygame.Rect(300, 245, 100, 10),
                  pygame.Rect(400, 245, 100, 10),
                  pygame.Rect(300, 345, 100, 10),
                  pygame.Rect(150, 345, 100, 10),
                  pygame.Rect(150, 295, 100, 10),
                  pygame.Rect(350, 95, 100, 10)]

    rects_rot = [pygame.Rect(95, 0, 10, 100),
                 pygame.Rect(95, 100, 10, 100),
                 pygame.Rect(145, 0, 10, 100),
                 pygame.Rect(145, 100, 10, 100),
                 pygame.Rect(195, -50, 10, 100),
                 pygame.Rect(195, 50, 10, 100),
                 pygame.Rect(195, 50, 10, 100),
                 pygame.Rect(295, 50, 10, 100),
                 pygame.Rect(395, 150, 10, 100),
                 pygame.Rect(295, 250, 10, 100),
                 pygame.Rect(245, 350, 10, 100),
                 pygame.Rect(95, 300, 10, 100)]

    rects = rects_rot + rects_vert

    def blit_wall(self, coords, n, rot):
        n = (pygame.time.get_ticks() + n * 300) % 1200
        display = self.display
        if rot == 1:
            if 0 <= n < 300:
                display.blit(self.wall1, coords)
            elif 300 <= n < 600:
                display.blit(self.wall2, coords)
            elif 600 <= n < 900:
                display.blit(self.wall4, coords)
            elif 900 <= n < 1200:
                display.blit(self.wall5, coords)
        else:
            if 0 <= n < 300:
                display.blit(pygame.transform.rotate(self.wall1, 90), coords)
            elif 300 <= n < 600:
                display.blit(pygame.transform.rotate(self.wall4, 90), coords)
            elif 600 <= n < 900:
                display.blit(pygame.transform.rotate(self.wall2, 90), coords)
            elif 900 <= n < 1200:
                display.blit(pygame.transform.rotate(self.wall5, 90), coords)

    def show_labirint(self):
        q = 0
        for rect in self.rects_rot:
            q += 1
            self.blit_wall(rect, q % 4 + 1, 0)

        for rect in self.rects_vert:
            q += 1
            self.blit_wall(rect, q % 4 + 1, 1)


class Leha(Main):
    def __init__(self, w, c):
        self.walls_object = w
        self.coins_object = c

    lesha = pygame.image.load('img/petrov_detail.png')
    leha = pygame.transform.scale(lesha, (34, 45))
    leha_rect = leha.get_rect(topleft=(0, 0))
    sound1 = pygame.mixer.Sound('sounds_and_music/sounds/Pickup_Coin10.wav')
    sound2 = pygame.mixer.Sound('sounds_and_music/sounds/Explosion.wav')

    SPEED = 1
    coins = 0

    def is_collision_wall(self):
        for wall in self.walls_object.rects:
            if self.leha_rect.colliderect(wall):
                self.sound2.play()
                self.leha_rect.topleft = (0, 0)
                self.coins = 0
                self.coins_object.gotten_coins = []

    def is_collision_coin(self):
        for coin in self.coins_object.coins_rect:
            if self.leha_rect.colliderect(coin):
                if coin not in self.coins_object.gotten_coins:
                    self.sound1.play()
                    self.coins += 1
                    self.coins_object.gotten_coins.append(coin)

    def leha_move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.leha_rect.left > 0:
            self.leha_rect.x -= self.SPEED
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.leha_rect.right < 500:
            self.leha_rect.x += self.SPEED
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.leha_rect.bottom < 400:
            self.leha_rect.y += self.SPEED
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and self.leha_rect.top > 0:
            self.leha_rect.y -= self.SPEED

    def blit_lesha(self):
        self.display.blit(self.leha, self.leha_rect)


class Labirint(Main):
    walls_logic = Walls()
    coins_logic = Coins()
    lesha_logic = Leha(walls_logic, coins_logic)

    is_running = False

    def run(self):
        music_labirint = pygame.mixer.Sound('sounds_and_music/music/nlo-misticheskaya-muzyka_(mp3IQ.net).mp3')
        music_labirint.set_volume(0.04)
        music_labirint.play()
        display = self.display
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if self.lesha_logic.leha_rect.collidepoint((498, 398)):
                display.fill("#04548c")
                music_labirint.stop()
                self.is_running = False

            else:
                display.fill("#1e2045")
                display.blit(self.jetpack_img, (450, 350))

                self.walls_logic.show_labirint()

                self.coins_logic.blit_coins()

                self.lesha_logic.is_collision_wall()
                self.lesha_logic.leha_move()
                self.lesha_logic.blit_lesha()
                self.lesha_logic.is_collision_coin()

            pygame.display.update()
            self.clock.tick(110)
