from parent_class import Main
import game_rules
import pygame


class FirstScene(Main):

    def run(self):
        scene1_replicas = self.get_replics('dialogs/first_scene.txt')
        self.music_one.play()
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    self.i += 1
            if self.i < 6:
                self.display.fill("#04388c")

                self.display.blit(self.lesha, (0, 0))
                self.display.blit(self.alien, (320, 0))

                direction = scene1_replicas[self.i][0]

                self.display_window(direction, scene1_replicas[self.i][1:])
            elif self.i > 6:
                self.music_one.stop()
                self.display.fill("#04548c")
                self.is_running = False
            if self.i == 6:
                self.display.fill("#04548c")
                self.display_window("no", game_rules.labirint_rules, 20, 100)

            pygame.display.update()
            self.clock.tick(110)
