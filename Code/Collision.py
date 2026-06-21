import pygame

from Code.Obstacle import Obstacle
from Code.Player import Player


class Collision:

    @staticmethod
    def verify(entity_list):
        players = []
        for ent in entity_list:
            if isinstance(ent, Player):
                players.append(ent)
        obstacles = [ent for ent in entity_list if isinstance(ent, Obstacle)]
        for player in players:
            for obstacle in obstacles:
                if player.rect.colliderect(obstacle.rect):
                    player.take_damage(obstacle.damage)

    @staticmethod
    def remove(entity_list):
        remove_list = []
        for ent in entity_list:
            # Player morreu
            if isinstance(ent, Player):
                if ent.health <= 0:
                    remove_list.append(ent)
            # Obstáculo saiu da tela
            elif isinstance(ent, Obstacle):
                if ent.rect.right < 0:
                    remove_list.append(ent)
        for ent in remove_list:
            if ent in entity_list:
                entity_list.remove(ent)