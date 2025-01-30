import pygame

pygame.init()


class Main:
    sound1 = pygame.mixer.Sound('sounds_and_music/Hit_Hurt7.wav')
    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 12)
    display = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('DD GAME')
    clock = pygame.time.Clock()
    window = pygame.image.load('img/plash.png')
    windowR = pygame.image.load('img/right.png')
    windowL = pygame.image.load('img/left.png')
    lesha = pygame.image.load('img/lesha.png')
    lesha = pygame.transform.scale(lesha, (200, 400))
    alien = pygame.image.load('img/alien.png')
    alien = pygame.transform.scale(alien, (200, 400))
    admin = pygame.image.load('img/admin.png')
    admin = pygame.transform.scale(admin, (200, 400))

    i = 0
    is_running = True

    jetpack_img = pygame.transform.scale(pygame.image.load(f"img/jetpack.png"), (50, 50))

    def display_window(self, rotation, text, x=170, y=65):
        if rotation == "l":
            self.display.blit(self.windowL, (135, 50))
        elif rotation == "r":
            self.display.blit(self.windowR, (135, 50))
        elif rotation != "no":
            self.display.blit(self.window, (135, 50))

        strings = text.split("=")
        for i in range(0, len(strings)):
            j = i + 1
            y_i = y + 17 * j
            text_surface = self.font.render(f'{strings[i]}', True, (0, 0, 0))
            self.display.blit(text_surface, (x, y_i))

    def get_replics(self, namefile):
        scene_replics = []
        f = open(namefile, 'r', encoding='utf-8')
        for i in range(6):
            scene_replics.append(f.readline().replace("\n", ""))
        return scene_replics
