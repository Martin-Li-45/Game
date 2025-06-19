import pygame


'''Настройки экрана'''

WIDTH_SCREEN, HEIGHT_SCREEN = 1200, 800

MENU_TITLE_Y = 100
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_OFFSET_X = 100 
PLAY_BUTTON_Y = 260
EXIT_BUTTON_Y = 330
COLLISION_OFFSET = 50
FPS = 20

'''Настройки персонажа'''

SPAWN_LOCATION_1 = (150, 700)
SPAWN_LOCATION_2 = (1150, 700)
PLAYER_SPEED = 15
PLAYER_JUMP_POWER = -15
GRAVITY = 1

'''Настройки противника'''

ENEMY_SPEED = 4
DETECTION_RADIUS = 200
CHASE_SPEED = 3

'''Цвета'''

GREY = (100, 100, 100)
IRON_GREY = (67, 75, 77)
ANTHRACITE_GREY = (41, 49, 51)
QUARTZ_GREY = (108, 105, 96)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

'''Шрифты'''

PATH_FONT = 'fonts/Caveat-SemiBold.ttf'
SIZE_FONT = 40
COORDINATES_TEXT_CHAPTER = (40, 40)
COORDINATES_TEXT_VICTORY = (600, 500)

'''Изображения'''

ICON = pygame.image.load('images/icon.png')

JUMP_STEVE_1 = pygame.image.load('images/Steve/Jump_Steve-1.png')
JUMP_STEVE_2 = pygame.image.load('images/Steve/Jump_Steve-2.png')
JUMP_STEVE_3 = pygame.image.load('images/Steve/Jump_Steve-3.png')

MOVEMENT_STEVE_1 = pygame.image.load('images/Steve/Movement_Steve-1.png')
MOVEMENT_STEVE_2 = pygame.image.load('images/Steve/Movement_Steve-2.png')
MOVEMENT_STEVE_3 = pygame.image.load('images/Steve/Movement_Steve-3.png')
MOVEMENT_STEVE_4 = pygame.image.load('images/Steve/Movement_Steve-4.png')

STEVE_ATTACK_1 = pygame.image.load('images/Steve/Steve_Attack-1.png')
STEVE_ATTACK_2 = pygame.image.load('images/Steve/Steve_Attack-2.png')

STEVE_1 = pygame.image.load('images/Steve/Steve-1.png')
STEVE_2 = pygame.image.load('images/Steve/Steve-2.png')
STEVE_3 = pygame.image.load('images/Steve/Steve-3.png')
STEVE_4 = pygame.image.load('images/Steve/Steve-4.png')

ENEMY_1 = pygame.image.load('images/Enemy/Enemy-1.png')
ENEMY_2 = pygame.image.load('images/Enemy/Enemy-2.png')

MOVEMENT_ENEMY_1 = pygame.image.load('images/Enemy/Movement_Enemy-1.png')
MOVEMENT_ENEMY_2 = pygame.image.load('images/Enemy/Movement_Enemy-2.png')

BOSS = pygame.image.load('images/Boss/Boss.png')

SPIKE_IMAGE = pygame.image.load('images/Spike.png')
LOCK_IMAGE = pygame.image.load('images/Lock.png')
