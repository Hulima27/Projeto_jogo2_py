import pygame

from Code.Const import (
    ENTITY_SPEED,
    WIN_WIDTH,
    WIN_HEIGHT,
    PLAYER_KEY_UP,
    PLAYER_KEY_DOWN,
    PLAYER_KEY_LEFT,
    PLAYER_KEY_RIGHT,
)

from Code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Tempo de invencibilidade
        self.invincible = False
        self.invincible_time = 0

    def move(self):
        keys = pygame.key.get_pressed()
        # Movimento vertical
        if keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.y -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += ENTITY_SPEED[self.name]
        # Movimento horizontal
        if keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.x -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.x += ENTITY_SPEED[self.name]
        # Atualiza tempo de invencibilidade
        if self.invincible:
            if pygame.time.get_ticks() >= self.invincible_time:
                self.invincible = False

    def take_damage(self, damage):
        if self.invincible:
            return
        self.health -= damage
        self.invincible = True
        self.invincible_time = pygame.time.get_ticks() + 1000