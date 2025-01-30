import pygame
import random
from parent_class import Main


class Bird(Main):
    # SOUNDS
    sound1 = pygame.mixer.Sound('sounds_and_music/sounds/Jump3.wav')
    sound1.set_volume(0.05)
    sound2 = pygame.mixer.Sound('sounds_and_music/sounds/Explosion.wav')

    # GENERAL SETTINGS
    SPEED = 2
    GRAVITY = 1
    SCORE = 5  # столько надо набрать для прохождения игры
    SHRIFT = pygame.font.SysFont('arial', 36)

    offset = 0  # сдвиг колонн
    gap = 140  # расстояние между колоннами

    jump_time = 0
    jump_force = 0
    gravity_force = 1

    # PICTURES
    meteor_wall_bottom = pygame.image.load('img/meteor_wall.png')
    meteor_wall_bottom = pygame.transform.scale(meteor_wall_bottom, (100, 200))

    meteor_wall_top = pygame.image.load('img/meteor_wall.png')
    meteor_wall_top = pygame.transform.flip(meteor_wall_top, 1, 1)
    meteor_wall_top = pygame.transform.scale(meteor_wall_top, (100, 200))

    leha_img = pygame.image.load('img/leha_jetpack.png')
    leha_img = pygame.transform.scale(leha_img, (34, 45))

    background = pygame.image.load('img/sky.jpg')
    background = pygame.transform.scale(background, (500, 400))

    earth = pygame.image.load('img/earth.png')

    # RECTANGLES
    bird_rect = pygame.Rect((80, 178, 34, 45))

    earth_rect = pygame.Rect((0, 0, 320, 320))
    earth_rect.midleft = (500, 200)

    wall_top = pygame.Rect((300, 0 - offset, 100, 200))
    wall_bottom = pygame.Rect((300, 200 - offset + gap, 100, 200))

    def run(self):
        """
        Метод для запуска мини-игры "Птица"
        """
        music_bird = pygame.mixer.Sound('sounds_and_music/music/zemljane-trava-u-doma.mp3')
        music_bird.set_volume(0.06)
        music_bird.play()
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if (e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN) and (
                        self.SCORE > 0 or self.earth_rect.midleft[0] >= 100):
                    self.jump_time += 20
                    self.jump_force += 8
                    self.sound1.play()

            if self.SCORE > 0:
                self.display.blit(self.background, (0, 0))

                self.display.blit(self.leha_img, self.bird_rect)
                self.display.blit(self.meteor_wall_bottom, self.wall_bottom)
                self.display.blit(self.meteor_wall_top, self.wall_top)

                self.wall_top.x -= self.SPEED
                self.wall_bottom.x -= self.SPEED

                score_text = self.SHRIFT.render(f'{5 - self.SCORE}', True, 'white')
                self.display.blit(score_text, (10, 10))

                if self.bird_rect.top > 400:
                    self.bird_rect.bottom = 0
                    self.gravity_force = 1

                if self.jump_time > 0:
                    self.bird_rect.y -= self.jump_force
                    if self.jump_force > 1:
                        self.jump_force -= 1
                    self.jump_time -= 1
                    if self.jump_time == 0:
                        self.gravity_force = 1
                else:
                    self.gravity_force += 0.2
                    self.bird_rect.y += self.gravity_force

                if self.wall_top.right < 0:
                    offset = random.randint(0, 100)
                    gap = 140

                    self.wall_top = pygame.Rect((500, 0 - offset, 100, 200))
                    self.wall_bottom = pygame.Rect((500, 200 - offset + gap, 100, 200))
                    self.SCORE -= 1

                if self.wall_top.colliderect(self.bird_rect) or self.wall_bottom.colliderect(self.bird_rect):
                    self.sound2.play()
                    self.bird_rect = pygame.Rect((80, 178, 34, 45))
                    self.wall_top = pygame.Rect((600, 0 - self.offset, 100, 200))
                    self.wall_bottom = pygame.Rect((600, 200 - self.offset + self.gap, 100, 200))
                    self.SCORE = 5
            elif self.earth_rect.midleft[0] >= 100:
                self.display.blit(self.background, (0, 0))

                self.display.blit(self.leha_img, self.bird_rect)

                score_text = self.SHRIFT.render(f'{5 - self.SCORE}', True, 'white')
                self.display.blit(score_text, (10, 10))

                self.display.blit(self.earth, self.earth_rect)
                self.earth_rect.x -= 1

                if self.bird_rect.top > 250:
                    self.bird_rect.top = 250

                if self.jump_time > 0:
                    self.bird_rect.y -= self.jump_force
                    if self.jump_force > 1:
                        self.jump_force -= 1
                    self.jump_time -= 1
                    if self.jump_time == 0:
                        self.gravity_force = 1
                else:
                    self.gravity_force += 0.1
                    self.bird_rect.y += self.gravity_force
            else:
                music_bird.stop()
                self.is_running = False

            pygame.display.update()
            self.clock.tick(110)
