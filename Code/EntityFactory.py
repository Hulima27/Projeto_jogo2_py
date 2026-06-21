import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Obstacle import Obstacle
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):


        # FUNDO LEVEL 1

        if entity_name == "Level1bg":
            backgrounds = []
            for i in range(7):
                backgrounds.append(Background(f"Level1bg{i}", (0, 0)))
                backgrounds.append(
                    Background(f"Level1bg{i}", (WIN_WIDTH, 0)))
            return backgrounds


        # FUNDO LEVEL 2

        if entity_name == "Level2bg":
            backgrounds = []
            for i in range(5):
                backgrounds.append(Background(f"Level2bg{i}", (0, 0)))
                backgrounds.append(Background(f"Level2bg{i}", (WIN_WIDTH, 0)))
            return backgrounds


        # PLAYERS

        if entity_name == "Player1":
            return Player("Player1",(40, WIN_HEIGHT // 2))
        if entity_name == "Player2":
            return Player("Player2",(40, WIN_HEIGHT // 2 + 60))

        # OBSTÁCULO 1
        if entity_name == "Enemy1":
            return Obstacle("Enemy1",(WIN_WIDTH + 50,random.randint(20,WIN_HEIGHT - 70)))


        # OBSTÁCULO 2
        if entity_name == "Enemy2":
            return Obstacle("Enemy2",(WIN_WIDTH + 50,random.randint(20,WIN_HEIGHT - 70 )))