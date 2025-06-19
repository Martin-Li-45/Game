import pygame
import utils
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from sounds import Sounds
from texts import Text

def show_menu(screen):
    '''Меню'''
    font = Text().font
    
    while True:
        screen.fill(utils.ANTHRACITE_GREY)
        
        # Заголовок
        title = font.render("Моя Игра", True, utils.WHITE)
        screen.blit(title, (utils.WIDTH_SCREEN//2 - title.get_width()//2, utils.MENU_TITLE_Y))
        
        # Кнопка "Играть"
        play_button = pygame.Rect(utils.WIDTH_SCREEN//2 - utils.BUTTON_OFFSET_X, utils.PLAY_BUTTON_Y, 
                                utils.BUTTON_WIDTH, utils.BUTTON_HEIGHT)
        pygame.draw.rect(screen, utils.GREEN, play_button)
        play_text = font.render("Играть", True, utils.WHITE)
        screen.blit(play_text, (utils.WIDTH_SCREEN//2 - play_text.get_width()//2, utils.PLAY_BUTTON_Y))
        
        # Кнопка "Выход"
        exit_button = pygame.Rect(utils.WIDTH_SCREEN//2 - utils.BUTTON_OFFSET_X, utils.EXIT_BUTTON_Y, 
                                utils.BUTTON_WIDTH, utils.BUTTON_HEIGHT)
        pygame.draw.rect(screen, utils.RED, exit_button)
        exit_text = font.render("Выход", True, utils.WHITE)
        screen.blit(exit_text, (utils.WIDTH_SCREEN//2 - exit_text.get_width()//2, utils.EXIT_BUTTON_Y))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    return False
                
def main():
    pygame.init()
    screen = pygame.display.set_mode((utils.WIDTH_SCREEN, utils.HEIGHT_SCREEN))
    pygame.display.set_caption("Game") 
    pygame.display.set_icon(utils.ICON)
    clock = pygame.time.Clock()

    sounds = Sounds()   
    sounds.play_music()

    show_menu(screen)
   
    player = Player(utils.SPAWN_LOCATION_1)
    current_level_number = 1
    current_level = Level1(player, screen)

    run = True
    while run:
        clock.tick(utils.FPS)
        screen.fill(utils.GREY)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                run = False

        player.player_update(current_level.platforms)
        current_level.update()

        if player.rect.right > utils.WIDTH_SCREEN + utils.COLLISION_OFFSET:
            current_level_number += 1
            if current_level_number == 2:
                current_level = Level2(player, screen)
                player.respawn(utils.SPAWN_LOCATION_1)      

            elif current_level_number == 3:
                current_level = Level3(player, screen)
                player.respawn(utils.SPAWN_LOCATION_1) 

        elif player.rect.left < -utils.COLLISION_OFFSET:  
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

