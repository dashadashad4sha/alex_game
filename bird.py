import pygame
import random
from parent_class import Main


class Bird(Main):
    sound1 = pygame.mixer.Sound('sounds_and_music/Jump3.wav')
    sound1.set_volume(0.05)
    sound2 = pygame.mixer.Sound('sounds_and_music/Explosion.wav')

    SPEED = 2
    GRAVITY = 1
    SCORE = 5

    SHRIFT = pygame.font.SysFont('arial', 36)
    lhbrd = pygame.Rect((80, 178, 34, 45))

    earth_rect = pygame.Rect((0, 0, 320, 320))
    earth_rect.midleft = (500, 200)

    offset = 0
    gap = 140
    walltop = pygame.Rect((300, 0 - offset, 100, 200))
    wallbottom = pygame.Rect((300, 200 - offset + gap, 100, 200))

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

    earth = pygame.image.load('img/earth.png')
    is_running = False

    def run(self):
        pygame.mixer.music.load('sounds_and_music/zemljane-trava-u-doma.mp3')
        pygame.mixer.music.set_volume(0.06)
        pygame.mixer.music.play()
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

                self.display.blit(self.leha__img, self.lhbrd)
                self.display.blit(self.meteor_wall_bottom, self.wallbottom)
                self.display.blit(self.meteor_wall_top, self.walltop)

                self.walltop.x -= self.SPEED
                self.wallbottom.x -= self.SPEED

                score_text = self.SHRIFT.render(f'{5 - self.SCORE}', True, 'white')
                self.display.blit(score_text, (10, 10))

                if self.lhbrd.top > 400:
                    self.lhbrd.bottom = 0
                    self.gravity_force = 1

                if self.jump_time > 0:
                    self.lhbrd.y -= self.jump_force
                    if self.jump_force > 1:
                        self.jump_force -= 1
                    self.jump_time -= 1
                    if self.jump_time == 0:
                        self.gravity_force = 1
                else:
                    self.gravity_force += 0.2
                    self.lhbrd.y += self.gravity_force

                if self.walltop.right < 0:
                    offset = random.randint(0, 100)
                    gap = 140

                    self.walltop = pygame.Rect((500, 0 - offset, 100, 200))
                    self.wallbottom = pygame.Rect((500, 200 - offset + gap, 100, 200))
                    self.SCORE -= 1

                if self.walltop.colliderect(self.lhbrd) or self.wallbottom.colliderect(self.lhbrd):
                    self.sound2.play()
                    self.lhbrd = pygame.Rect((80, 178, 34, 45))
                    self.walltop = pygame.Rect((600, 0 - self.offset, 100, 200))
                    self.wallbottom = pygame.Rect((600, 200 - self.offset + self.gap, 100, 200))
                    self.SCORE = 5
            elif self.earth_rect.midleft[0] >= 100:
                self.display.blit(self.background, (0, 0))

                self.display.blit(self.leha__img, self.lhbrd)

                score_text = self.SHRIFT.render(f'{5 - self.SCORE}', True, 'white')
                self.display.blit(score_text, (10, 10))

                self.display.blit(self.earth, self.earth_rect)
                self.earth_rect.x -= 1

                if self.lhbrd.top > 250:
                    self.lhbrd.top = 250

                if self.jump_time > 0:
                    self.lhbrd.y -= self.jump_force
                    if self.jump_force > 1:
                        self.jump_force -= 1
                    self.jump_time -= 1
                    if self.jump_time == 0:
                        self.gravity_force = 1
                else:
                    self.gravity_force += 0.1
                    self.lhbrd.y += self.gravity_force
            else:
                self.is_running = False
                # self.display.fill("#120A8F")
                # self.display_window("no", "Ура вы на Земле!")
            pygame.display.update()
            self.clock.tick(110)
