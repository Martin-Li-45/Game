import pygame
import utils
from levels.puzzle import Puzzle
from texts import Text
from sounds import Sounds


class Level:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen 

        self.sounds = Sounds()
        self.text = Text()

        self.platforms = pygame.sprite.Group()    
        self.spikes = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
            
        self.enemies = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()

        self.puzzle_triggers = pygame.sprite.Group()
        self.pins = pygame.sprite.Group()
        self.puzzle = Puzzle(screen)
        self.puzzle_trigger_active = False
        self.puzzle_complite = False

        self.setup_level()

    def setup_level(self):
        """Загрузка уровеня"""
        pass

    def update(self):
        """Обновление всех объектов уровня"""
        self.platforms.update()
        self.spikes.update()
        self.obstacles.update()
        self.puzzle_triggers.update()
        self.enemies.update(self.player, self.platforms)
        self.bosses.update(self.player, self.platforms)

        if self.puzzle_trigger_active == True:
            self.puzzle.update()

    def draw(self):
        """Отрисовывка всех объектов уровня"""
        self.platforms.draw(self.screen)
        self.spikes.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.puzzle_triggers.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bosses.draw(self.screen)
        self.text.get_text(self.screen, self.chapter_number, utils.COORDINATES_TEXT_CHAPTER)  
        
        if self.puzzle_trigger_active == True:
            self.puzzle.draw()

    def check_collisions(self):
        for puzzle_trigger in self.puzzle_triggers:
            if self.player.rect.colliderect(puzzle_trigger.rect) and self.puzzle_complite == False:
                self.puzzle_trigger_active = True
                self.puzzle.running_puzzle()
                self.puzzle_complite = self.puzzle.check_puzzle_complite()
                if self.puzzle_complite:
                    self.obstacles.empty()
                    self.sounds.play_sound('lock')
            else:
                self.puzzle_trigger_active = False

        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.sounds.play_sound('death')
                if self.player.attack:
                    enemy.kill()
                else:
                    self.player.respawn(utils.SPAWN_LOCATION_1)

        for boss in self.bosses:
            if self.player.rect.colliderect(boss.rect) and self.player.on_ground:
                self.sounds.play_sound('death')
                self.player.respawn(utils.SPAWN_LOCATION_1)
        
        for spike in self.spikes:
            if self.player.rect.colliderect(spike.rect):
               self.sounds.play_sound('death')
               self.player.respawn(utils.SPAWN_LOCATION_1) 

        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
               self.sounds.play_sound('death')
               self.player.respawn(utils.SPAWN_LOCATION_1) 
                    
                

