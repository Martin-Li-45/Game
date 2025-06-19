import pygame
import utils


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, trajectory):
        super().__init__()

        self.animations = {
            'inactive': [utils.ENEMY_1, utils.ENEMY_2],
            'walk': [utils.MOVEMENT_ENEMY_1, utils.MOVEMENT_ENEMY_2]
        }
        
        self.current_animation = 'walk' 
        self.animation_frame = 0
        self.image = self.animations[self.current_animation][0]
        
        self.position = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.rect = self.image.get_rect(midbottom=self.position)
        self.hitbox = pygame.Rect(0, 0, 28, 60)
        self.hitbox.midbottom = self.rect.midbottom
        
        self.waypoint_boxes = []
        for point in trajectory:
            waypoint = pygame.Rect(0, 0, 10, 10)  
            waypoint.center = point
            self.waypoint_boxes.append(waypoint)
            
        self.current_waypoint = 0
        self.speed = utils.ENEMY_SPEED  
        self.detection_radius = utils.DETECTION_RADIUS
        self.chase_speed = utils.CHASE_SPEED
        
        self.gravity = utils.GRAVITY
        self.on_ground = False
        self.facing_right = True
    
    def update_hitbox(self):
        '''Синхронизирует хитбокс с позицией спрайта'''
        self.hitbox.midbottom = self.rect.midbottom
    
    def check_collisions(self, platforms):
        '''Обработка столкновений с платформами'''
        self.on_ground = False
        old_pos = self.rect.copy()
        
        for platform in platforms:
            if not self.rect.colliderect(platform.rect):
                continue
                
            # Вертикальные столкновения
            if abs(old_pos.bottom - platform.rect.top) < 10:
                self.rect.bottom = platform.rect.top
                self.on_ground = True
                self.vel.y = 0
            elif abs(old_pos.top - platform.rect.bottom) < 10:
                self.rect.top = platform.rect.bottom
                self.vel.y = 0
            
            # Горизонтальные столкновения
            if abs(old_pos.right - platform.rect.left) < 10:
                self.rect.right = platform.rect.left
                self.vel.x = 0
            elif abs(old_pos.left - platform.rect.right) < 10:
                self.rect.left = platform.rect.right
                self.vel.x = 0
        
        self.position = pygame.math.Vector2(self.rect.midbottom)

    def get_current_status(self, player):
        '''Получение текущего статуса'''
        distance = pygame.math.Vector2(player.rect.center).distance_to(self.rect.center)
        
        if distance <= self.detection_radius and abs(player.rect.centery - self.rect.centery) < 100:
            self.chase_player(player)
        else:
            self.patrol()
    
    def chase_player(self, player):
        '''Преследование игрока'''
        direction = pygame.math.Vector2(player.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() > 0:
            direction = direction.normalize()
        
        self.vel.x = direction.x * self.chase_speed
        self.facing_right = direction.x > 0
        
        if player.rect.top < self.rect.top - 30 and self.on_ground:
            self.vel.y = -12
    
    def patrol(self):
        '''Движение между точками с использованием хитбоксов'''
        if not self.waypoint_boxes:
            return
            
        target = self.waypoint_boxes[self.current_waypoint]
        
        # Движение по X
        if self.hitbox.centerx < target.centerx:
            self.vel.x = self.speed
            self.facing_right = True
        elif self.hitbox.centerx > target.centerx:
            self.vel.x = -self.speed
            self.facing_right = False
        else:
            self.vel.x = 0
            
        # Движение по Y (если точки на разных высотах)
        if self.hitbox.centery < target.centery:
            self.vel.y = self.speed
        elif self.hitbox.centery > target.centery:
            self.vel.y = -self.speed
        else:
            self.vel.y = 0
            
        # Проверка достижения точки
        if self.hitbox.colliderect(target):
            self.current_waypoint = (self.current_waypoint + 1) % len(self.waypoint_boxes)

    def animate(self):
        '''Анимирование противника'''
        animation = self.animations[self.current_animation]
        self.animation_frame += 0.15
        
        if self.animation_frame >= len(animation):
            self.animation_frame = 0
        
        self.image = animation[int(self.animation_frame)]
        
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def apply_physics(self):
        '''Применение физики к противнику'''
        if not self.on_ground:
            self.vel.y += self.gravity
        
        self.position += self.vel
        self.rect.midbottom = self.position

    def update(self, player, platforms):
        self.get_current_status(player)
        self.apply_physics()
        self.check_collisions(platforms)
        self.animate()
        self.update_hitbox()
