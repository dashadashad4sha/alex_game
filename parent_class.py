import pygame

pygame.init()


class Main:
    # COMMON MUSIC
    music_one = pygame.mixer.Sound('sounds_and_music/music/scene1music.mp3')
    music_one.set_volume(0.20)

    # FONT
    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 12)

    # GAME SETTINGS
    display = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('DD GAME')
    clock = pygame.time.Clock()

    # PICTURES
    window = pygame.image.load('img/plashes/plash.png')
    windowR = pygame.image.load('img/plashes/right.png')
    windowL = pygame.image.load('img/plashes/left.png')
    lesha = pygame.image.load('img/lesha.png')
    lesha = pygame.transform.scale(lesha, (200, 400))
    alien = pygame.image.load('img/alien.png')
    alien = pygame.transform.scale(alien, (200, 400))
    admin = pygame.image.load('img/admin.png')
    admin = pygame.transform.scale(admin, (200, 400))
    jetpack_img = pygame.transform.scale(pygame.image.load(f"img/jetpack.png"), (50, 50))
    filarmonia = pygame.image.load('img/filarmonia.png')
    filarmonia = pygame.transform.scale(filarmonia, (400, 400))

    i = 0
    is_running = True

    def display_window(self, rotation, text, x=170, y=65):
        """
        Метод для отображения диалогов.

        :param rotation: направление плашки
        :param text: текст
        :param x: абсцисса левого верхнего угла плашки
        :param y: ордината левого верхнего угла плашки
        """
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
        """
        Метод для преобразования файла с репликами
        в список с отдельными строками
        без символов переноса строки.

        :param namefile: относительный путь к файлу с репликами
        :return: list
        """
        scene_replics = []
        f = open(namefile, 'r', encoding='utf-8')
        for i in range(6):
            scene_replics.append(f.readline().replace("\n", ""))
        return scene_replics
