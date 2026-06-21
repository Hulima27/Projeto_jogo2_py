import pygame

from Code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    MENU_OPTION
)

from Code.Menu import Menu
from Code.Level import Level


class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Escape Run")
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            option = menu.run()
            if option == MENU_OPTION[0]:

                # 1 jogador
                level = Level(self.window,"level1",players=1)

                result = level.run()

                if result == "NEXT_LEVEL":
                    level = Level(self.window,"level2",players=1)

                    level.run()

            elif option == MENU_OPTION[1]:
                # 2 jogadores
                level = Level(self.window,"level1",players=2)
                result = level.run()

                if result == "NEXT_LEVEL":
                    level = Level(self.window,"level2",players=2)
                    level.run()
            elif option == MENU_OPTION[2]:
                pygame.quit()
                return