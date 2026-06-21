import pygame
from abc import ABC, abstractmethod

from Code.Const import ENTITY_DAMAGE, ENTITY_HEALTH


class Entity(ABC):
    """
    Classe base de todas as entidades do jogo.
    """

    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carrega a imagem
        self.surf = pygame.image.load(f'./asset/{self.name}.png').convert_alpha()
        # Define posição
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        # Atributos
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self):
        """
        Método obrigatório para todas as entidades.
        """
        pass

    def draw(self, window):
        """
        Desenha a entidade na tela.
        """
        window.blit(self.surf, self.rect)
    def is_alive(self):
        """
        Retorna True caso a entidade esteja viva.
        """
        return self.health > 0