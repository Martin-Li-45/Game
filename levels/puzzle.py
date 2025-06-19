import pygame
import random
import utils
from sounds import Sounds

class PuzzleTrigger(pygame.sprite.Sprite):
   def __init__(self, x, y):
      super().__init__() 

      self.image = utils.LOCK_IMAGE

      self.rect = self.image.get_rect(topleft=(x, y))
      
class Pin(pygame.sprite.Sprite):
   def __init__(self, pin_x, pin_y):
      super().__init__()

      self.image = pygame.Surface((100, 200))
      self.image.fill(utils.ANTHRACITE_GREY) 

      self.rect = self.image.get_rect(topleft=(pin_x, pin_y))



class Puzzle:
   def __init__(self, screen):
      super().__init__()

      self.screen = screen
      self.sounds = Sounds()
      self.pins = pygame.sprite.Group()
      self.pin_positions = []

      for x in range(250, 851, 150):
         y = random.choice(range(150, 351, 50))
         self.pin_positions.append([x, y])
         self.pins.add(Pin(x, y))

      
   def running_puzzle(self):
      mouse_pressed = pygame.mouse.get_pressed()[0]
      mouse_pos = pygame.mouse.get_pos()
      
      if mouse_pressed and not self.click_processed:
         for i, (x, y) in enumerate(self.pin_positions):
            pin_rect = pygame.Rect(x, y, 100, 200)
            if pin_rect.collidepoint(mouse_pos):
               self.sounds.play_sound('pin')
               # Перемещаем пин
               if y + 50 < 351:
                  self.pin_positions[i][1] += 50
               else:
                  self.pin_positions[i][1] = 150
               self.click_processed = True
               break
      elif not mouse_pressed:
         self.click_processed = False




   def update(self):
      """Обновление состояния пинов"""
      self.pins.empty()
      for x, y in self.pin_positions:
         self.pins.add(Pin(x, y))

   def draw(self):
      """Отрисовка всех элементов"""
      pygame.draw.rect(self.screen, utils.QUARTZ_GREY, (150, 100, 900, 500))
      pygame.draw.rect(self.screen, utils.BLACK, (200, 445, 800, 5))
      self.pins.draw(self.screen)                   

   def check_puzzle_complite(self):
      if all(pin_y == 250 for (pin_x, pin_y) in self.pin_positions):
         return True
      else:
         return False
   
