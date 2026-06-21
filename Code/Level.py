import random
import sys
import pygame

from Code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    FPS,
    COLOR_WHITE,
    COLOR_GREEN,
    COLOR_RED,
    LEVEL_TIME,
    SPAWN_TIME,
    EVENT_OBSTACLE
)

from Code.EntityFactory import EntityFactory
from Code.Collision import Collision
from Code.Player import Player


class Level:

    def __init__(self, window, level_name, players):
        self.window = window
        self.level_name = level_name
        self.entities = []

        # BACKGROUND

        if level_name == "level1":
            self.entities.extend(
                EntityFactory.get_entity("Level1bg"))
        else:
            self.entities.extend(
                EntityFactory.get_entity("Level2bg"))


        # PLAYER

        # PLAYER

        self.players = players

        self.player1 = EntityFactory.get_entity("Player1")
        self.entities.append(self.player1)

        if self.players == 2:
            self.player2 = EntityFactory.get_entity("Player2")
            self.entities.append(self.player2)


        # TIMER

        self.level_time = LEVEL_TIME[level_name]
        pygame.time.set_timer(
            EVENT_OBSTACLE,
            SPAWN_TIME[level_name]
        )

        # Música da fase
        pygame.mixer.music.load(
            f"./asset/{level_name}.wav")
        pygame.mixer.music.play(-1)


    def draw_text(self,text,size,color,x,y):
        font = pygame.font.SysFont("Arial",size,True)
        surface = font.render(text,True,color)
        self.window.blit(surface,(x, y))

    def draw_life_bar(self):
        # Player 1
        pygame.draw.rect(self.window, COLOR_RED, (10, 10, 200, 20))
        pygame.draw.rect(self.window,COLOR_GREEN,(10, 10, self.player1.health * 2, 20))
        # Player 2
        if self.players == 2:
            pygame.draw.rect(self.window, COLOR_RED, (10, 40, 200, 20))
            pygame.draw.rect(self.window,COLOR_GREEN,(10, 40, self.player2.health * 2, 20))


    def spawn_obstacle(self):
        obstacle = random.choice(("Enemy1","Enemy2"))
        self.entities.append(EntityFactory.get_entity(obstacle))


    def update(self, dt):
        self.level_time -= dt
        for entity in self.entities:
            entity.move()
        Collision.verify(self.entities)
        Collision.remove(self.entities)



    def draw(self):
        self.window.fill((0, 0, 0))

        # Desenha todas as entidades

        for entity in self.entities:
            entity.draw(self.window)
        # Barra de vida
        self.draw_life_bar()
        # Vida
        self.draw_text(f"P1: {self.player1.health}",18,COLOR_WHITE,10,40)
        if self.players == 2:
            self.draw_text(f"P2: {self.player2.health}",18,COLOR_WHITE,10,65)
            tempo_y = 90
        else:
            tempo_y = 65
        self.draw_text(f"Tempo: {self.level_time // 1000}",18,COLOR_WHITE,10,tempo_y)

        # Tempo
        self.draw_text(f"Tempo: {self.level_time // 1000}",18,COLOR_WHITE,10,tempo_y)
        # Fase
        self.draw_text(self.level_name.upper(),18,COLOR_WHITE,WIN_WIDTH-110,10)



    def show_message(self, title, subtitle=""):

        self.window.fill((0, 0, 0))

        font1 = pygame.font.SysFont("Arial", 40, True)
        font2 = pygame.font.SysFont("Arial", 22)

        title_surface = font1.render(title, True, COLOR_WHITE)
        title_rect = title_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 20))

        self.window.blit(title_surface, title_rect)

        if subtitle != "":
            subtitle_surface = font2.render(subtitle, True, COLOR_WHITE)
            subtitle_rect = subtitle_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 25))
            self.window.blit(subtitle_surface, subtitle_rect)

        pygame.display.flip()
        pygame.time.delay(2500)


    def run(self):
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(FPS)

            # EVENTOS


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_OBSTACLE:
                    self.spawn_obstacle()


            # ATUALIZA O JOGO


            self.update(dt)
            self.draw()
            pygame.display.flip()


            # GAME OVER

            if self.players == 1:
                if self.player1.health <= 0:
                    self.show_message("GAME OVER")
                    return "GAME_OVER"
            else:
                if self.player1.health <= 0 and self.player2.health <= 0:
                    self.show_message("GAME OVER")
                    return "GAME_OVER"


            # LEVEL COMPLETO


            if self.level_time <= 0:
                if self.level_name == "level1":
                    self.show_message("LEVEL COMPLETE","Prepare-se para a Fase 2")
                    return "NEXT_LEVEL"
                else:
                    self.show_message("FIM DA BETA!","Parabens!")
                    return "WIN"