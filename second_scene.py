from parent_class import Main
import game_rules
import pygame


class SecondScene(Main):

    def run(self):
        scene2_replicas = self.get_replics('dialogs/second_scene.txt')
        self.music_one.play()
        while self.is_running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    self.i += 1

            if self.i < 4:
                self.display.fill("#04388c")
                self.display.blit(self.lesha, (0, 0))
                direction = scene2_replicas[self.i][0]
                self.display_window(direction, scene2_replicas[self.i][1:])
                if self.i == 3:
                    self.display.blit(pygame.transform.scale(self.jetpack_img, (200, 200)), (320, 50))
            elif self.i == 4:
                self.display.fill("#04548c")
                self.display_window("no", game_rules.bird_rules, 20, 100)
            else:
                self.music_one.stop()
                self.is_running = False

            pygame.display.update()
            self.clock.tick(110)
