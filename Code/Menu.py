import pygame

from Code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    COLOR_WHITE,
    COLOR_YELLOW,
    COLOR_ORANGE,
    MENU_OPTION
)


class Menu:

    def __init__(self, window):

        self.window = window
        self.background = pygame.image.load("./asset/Menu (7).png").convert()
        self.background = pygame.transform.scale(self.background,(WIN_WIDTH, WIN_HEIGHT))
        self.selected = 0

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size,bold=True)
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(x, y))
        self.window.blit(surface, rect)

    def run(self):
        pygame.mixer.music.load("./asset/Menupiano.wav")
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.blit(self.background, (0, 0))

            # TÍTULO

            self.draw_text("ESCAPE",42,COLOR_ORANGE,WIN_WIDTH // 2,55)
            self.draw_text("RUN",42,COLOR_ORANGE,WIN_WIDTH // 2,95)


            # OPÇÕES

            for i, option in enumerate(MENU_OPTION):
                color = COLOR_YELLOW if i == self.selected else COLOR_WHITE
                self.draw_text(option,22,color,WIN_WIDTH // 2,190 + i * 35)


            # CONTROLES

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected -= 1
                        if self.selected < 0:
                            self.selected = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_DOWN:
                        self.selected += 1
                        if self.selected >= len(MENU_OPTION):
                            self.selected = 0
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.selected]
            pygame.display.flip()