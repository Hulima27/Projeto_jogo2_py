import pygame

# JANELA

WIN_WIDTH = 576
WIN_HEIGHT = 324
FPS = 60

# CORES

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (220, 20, 60)
COLOR_GREEN = (50, 205, 50)
COLOR_YELLOW = (255, 222, 33)
COLOR_ORANGE = (255, 128, 0)


# EVENTOS

EVENT_OBSTACLE = pygame.USEREVENT + 1


# TEMPO DAS FASES (ms)

LEVEL_TIME = {
    "level1": 30000,   # 30 segundos
    "level2": 45000    # 45 segundos
}


# SPAWN DOS OBSTÁCULOS

SPAWN_TIME = {
    "level1": 1800,
    "level2": 1100
}


# VELOCIDADE DAS ENTIDADES

ENTITY_SPEED = {

    # PLAYER
    "Player1": 4,
    "Player2": 4,


    # OBSTÁCULOS
    "Enemy1": 4,
    "Enemy2": 6,

    # LEVEL 1
    "Level1bg0": 0,
    "Level1bg1": 1,
    "Level1bg2": 2,
    "Level1bg3": 3,
    "Level1bg4": 4,
    "Level1bg5": 5,
    "Level1bg6": 6,

    # LEVEL 2
    "Level2bg0": 0,
    "Level2bg1": 2,
    "Level2bg2": 3,
    "Level2bg3": 4,
    "Level2bg4": 5,
    "Level2bg5": 6
}


# VIDA

ENTITY_HEALTH = {

    "Player1": 100,
    "Player2": 100,

    "Enemy1": 9999,
    "Enemy2": 9999,

    "Level1bg0": 9999,
    "Level1bg1": 9999,
    "Level1bg2": 9999,
    "Level1bg3": 9999,
    "Level1bg4": 9999,
    "Level1bg5": 9999,
    "Level1bg6": 9999,

    "Level2bg0": 9999,
    "Level2bg1": 9999,
    "Level2bg2": 9999,
    "Level2bg3": 9999,
    "Level2bg4": 9999,
    "Level2bg5": 9999,
}


# DANO

ENTITY_DAMAGE = {

    "Player1": 0,
    "Player2": 0,

    "Enemy1": 20,
    "Enemy2": 35,

    "Level1bg0": 0,
    "Level1bg1": 0,
    "Level1bg2": 0,
    "Level1bg3": 0,
    "Level1bg4": 0,
    "Level1bg5": 0,
    "Level1bg6": 0,

    "Level2bg0": 0,
    "Level2bg1": 0,
    "Level2bg2": 0,
    "Level2bg3": 0,
    "Level2bg4": 0,
    "Level2bg5": 0,
}


# CONTROLES

PLAYER_KEY_UP = {
    "Player1": pygame.K_w,
    "Player2": pygame.K_UP
}

PLAYER_KEY_DOWN = {
    "Player1": pygame.K_s,
    "Player2": pygame.K_DOWN
}

PLAYER_KEY_LEFT = {
    "Player1": pygame.K_a,
    "Player2": pygame.K_LEFT
}

PLAYER_KEY_RIGHT = {
    "Player1": pygame.K_d,
    "Player2": pygame.K_RIGHT
}


# MENU

MENU_OPTION = (
    "NEW GAME 1P",
    "NEW GAME 2P",
    "EXIT"
)