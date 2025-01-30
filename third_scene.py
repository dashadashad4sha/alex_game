from parent_class import Main
import game_rules
import pygame


class ThirdScene(Main):

    def run(self):
        pygame.mixer.music.load('sounds_and_music/music/scene1music.mp3')
        pygame.mixer.music.set_volume(0.20)
        pygame.mixer.music.play()
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    self.i += 1
            if self.i < 1:
                self.display.fill("#04548c")

                self.display_window("no", "Ура вы на Земле!")

            elif self.i > 1:
                pygame.mixer.music.stop()
                self.display.fill("#04548c")
                self.is_running = False
            if self.i == 1:
                self.display_window("no", game_rules.races_rules, 20, 100)

            pygame.display.update()
            self.clock.tick(110)
