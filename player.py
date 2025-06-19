import pygame
import utils
from sounds import Sounds


class Player(pygame.sprite.Sprite):
    def __init__(self, start_position):
        super().__init__()
        self.animations = {
            'inactive': [utils.STEVE_1, utils.STEVE_2, utils.STEVE_3, utils.STEVE_4],  
            'run':  [utils.MOVEMENT_STEVE_1, utils.MOVEMENT_STEVE_2, utils.MOVEMENT_STEVE_3, utils.MOVEMENT_STEVE_4],
            'jump': [utils.JUMP_STEVE_1, utils.JUMP_STEVE_2, utils.JUMP_STEVE_3],
            'attack': [utils.STEVE_ATTACK_1, utils.STEVE_ATTACK_2]
        }

        self.current_status = 'inactive'
        self.animation_frame = 0
        self.image = self.animations[self.current_status][0]

        self.start_position = start_position
        self.position = pygame.math.Vector2(self.start_position)
        self.vel = pygame.math.Vector2(0, 0)
        self.rect = self.image.get_rect(midbottom=self.position)

        self.speed = utils.PLAYER_SPEED
        self.jump_power = utils.PLAYER_JUMP_POWER
        self.gravity = utils.GRAVITY
        self.on_ground = True
        self.attack = False 

        self.sounds = Sounds()
        
    def check_collisions(self, platforms):
        '''Обработка столкновений с платформами'''
        old_position = self.rect.copy()
        
        self.on_ground = False
        
        self.rect.x = round(self.rect.x + self.vel.x)
        self.rect.y = round(self.rect.y + self.vel.y)
        
        # Проверка коллизий с каждой платформой
        for platform in platforms:
            if not self.rect.colliderect(platform.rect):
                continue
                
            # ВЕРТИКАЛЬНЫЕ КОЛЛИЗИИ
            if abs(old_position.bottom - platform.rect.top) < 10:  # Сверху
                self.rect.bottom = platform.rect.top
                self.on_ground = True
                self.vel.y = 0
            elif abs(old_position.top - platform.rect.bottom) < 10:  # Снизу
                self.rect.top = platform.rect.bottom
                self.vel.y = 0
            
            # ГОРИЗОНТАЛЬНЫЕ КОЛЛИЗИИ
            if abs(old_position.right - platform.rect.left) < 10:  # Справа
                self.rect.right = platform.rect.left
                self.vel.x = 0
            elif abs(old_position.left - platform.rect.right) < 10:  # Слева
                self.rect.left = platform.rect.right
                self.vel.x = 0
        
        # Дополнительная проверка земли (анти-проваливание)
        if not self.on_ground:
            test_rect = self.rect.copy()
            test_rect.y += 2 
            for platform in platforms:
                if test_rect.colliderect(platform.rect):
                    if test_rect.bottom <= platform.rect.top + 5:
                        self.rect.bottom = platform.rect.top
                        self.on_ground = True
                        self.vel.y = 0
                        break

    def get_current_status(self):
        '''Получение текущего статуса персонажа'''
        if not self.on_ground:      
            self.current_status = 'jump'
        elif self.vel.x != 0 and not self.attack:       
            self.current_status = 'run'
        elif self.attack:
            self.current_status = 'attack'
        else:                       
            self.current_status = 'inactive'

    def animate(self):
        '''Анимирование персонажа'''
        animation = self.animations[self.current_status]
        self.animation_frame += 0.15

        if self.animation_frame >= len(animation):
            self.animation_frame = 0

        self.image = animation[int(self.animation_frame)]
    
    def get_input(self):
        '''Считывание клавишь для управления персонажем'''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vel.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel.x = self.speed 
        elif keys[pygame.K_e]:
            self.attack = True
        else:
            self.vel.x = 0 
            self.attack = False

        if keys[pygame.K_SPACE] and self.on_ground:
            self.sounds.play_sound('jump')
            self.vel.y = self.jump_power
            self.on_ground = False

    def apply_physics(self):
        '''Применение физики к персонажу'''
        if self.on_ground == False:
            self.vel.y += self.gravity
        self.position += self.vel

        if self.position.y >= 700:
            self.position.y = 700
            self.vel.y = 0
            self.on_ground = True


        self.rect.midbottom = self.position

    def respawn(self, position_respawn):
        """Телепортация игрока в определенную позицию"""
        self.position = pygame.math.Vector2(position_respawn)
        self.vel = pygame.math.Vector2(0, 0)
        self.rect.midbottom = self.position

    def player_update(self, platforms):
        '''Обновление персонажа'''
        self.get_input()
        self.check_collisions(platforms)
        self.apply_physics()
        self.get_current_status()
        self.animate()
