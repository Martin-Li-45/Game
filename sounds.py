import pygame


class Sounds:
    def __init__(self):
        '''Звуки'''
        pygame.mixer.init()

        self.sounds = {
            'jump': pygame.mixer.Sound('sounds/jump.mp3'),
            'death': pygame.mixer.Sound('sounds/death.mp3'),
            'lock': pygame.mixer.Sound('sounds/lock.mp3'),
            'pin': pygame.mixer.Sound('sounds/pin.mp3'),
            'attack': pygame.mixer.Sound('sounds/attack.mp3')
        }

    def play_music(self):
        """Запуск фоновой музыки"""
        pygame.mixer.music.load('sounds/background music.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1) 

    def play_sound(self, name):
        """Воспроизведение звукового эффекта"""
        self.sounds[name].play()