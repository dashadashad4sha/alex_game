from labirint import Leha
from parent_class import Main
import game_rules
import pygame


class FinalScene(Main):
    filarmonia_rect = pygame.Rect((0, 0, 400, 400))
    filarmonia_rect.midbottom = (250, 350)
    filarmonia = pygame.image.load('img/filarmonia.png')
    filarmonia = pygame.transform.scale(filarmonia, (400, 450))
    organ = pygame.image.load('img/organ.png')
    organ = pygame.transform.scale(organ, (500, 400))
    lesha_logic = Leha(None, None)
    lesha_logic.leha_rect.center = (250, 380)

    doors = [pygame.Rect(250, 290, 50, 50), pygame.Rect(200, 290, 50, 50), pygame.Rect(70, 290, 50, 50),
             pygame.Rect(380, 290, 50, 50)]
    is_running = True

    leha_animation = 0

    def run(self):
        music_one = pygame.mixer.Sound('sounds_and_music/scene1music.mp3')
        music_one.set_volume(0.20)
        music_one.play()
        final_scene_replicas = self.get_replics('dialogs/final_scene.txt')

        teriam_music = pygame.mixer.Sound('sounds_and_music/teriam.mp3')
        teriam_music.set_volume(0.1)

        teriam_music_flag = True

        while self.is_running:
            self.display.fill('#CFCFDD')
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and 1 <= self.i <= 4:
                    self.i += 1
                if 5 == self.i and e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                    self.i += 1

            if self.i == 5 and teriam_music_flag:
                teriam_music_flag = False
                music_one.stop()
                teriam_music.play()

            if self.i == 0:
                self.display.blit(self.filarmonia, self.filarmonia_rect)
                self.lesha_logic.leha_move()
                self.lesha_logic.blit_lesha()

                for d in self.doors:
                    if d.collidepoint(self.lesha_logic.leha_rect.center):
                        self.i = 1

            elif 1 <= self.i <= 4:
                self.display.blit(self.organ, (0, 0))

                self.display.blit(self.lesha, (0, 0))
                self.display.blit(self.admin, (320, 0))

                direction = final_scene_replicas[self.i][0]

                self.display_window(direction, final_scene_replicas[self.i][1:])

            elif 5 == self.i:

                self.display.blit(self.organ, (0, 0))

                self.display.blit(
                    pygame.transform.rotate(pygame.transform.scale(self.lesha, (100, 200)),
                                            10 - self.leha_animation % 20),
                    (200, 130))
                self.leha_animation += 0.1

                if self.leha_animation >= 10:
                    self.display_window("no", "Нажмите Enter,= чтобы выйти.")

            else:
                pygame.mixer.music.stop()
                self.is_running = False

            pygame.display.update()
            self.clock.tick(110)


# ss = FinalScene()
# ss.run()
