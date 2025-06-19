import pygame
import utils
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from sounds import Sounds


def main():
    pygame.init()
    screen = pygame.display.set_mode((utils.WIDTH_SCREEN, utils.HEIGHT_SCREEN))
    pygame.display.set_caption("Game") 
    pygame.display.set_icon(utils.ICON)
    clock = pygame.time.Clock()

    sounds = Sounds()   
    sounds.play_music()
   
    player = Player(utils.SPAWN_LOCATION_1)
    current_level_number = 1
    current_level = Level1(player, screen)

    run = True
    while run:
        clock.tick(20)
        screen.fill(utils.GREY)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                run = False

        player.player_update(current_level.platforms)
        current_level.update()

        if player.rect.right > utils.WIDTH_SCREEN + 50:
            current_level_number += 1
            if current_level_number == 2:
                current_level = Level2(player, screen)
                player.respawn(utils.SPAWN_LOCATION_1)      

            elif current_level_number == 3:
                current_level = Level3(player, screen)
                player.respawn(utils.SPAWN_LOCATION_1) 

        elif player.rect.left < -50:  
            if current_level_number > 1: 
                current_level_number -= 1
            
                if current_level_number == 1:
                    current_level = Level1(player, screen)
                    player.respawn(utils.SPAWN_LOCATION_1)   
                elif current_level_number == 2:
                    current_level = Level2(player, screen)
                    player.respawn(utils.SPAWN_LOCATION_2) 

        current_level.check_collisions()
        current_level.draw()
        screen.blit(player.image, player.rect)
    
        pygame.display.update()


if __name__ == "__main__":
    main()

