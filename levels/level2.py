from levels.level import Level
from levels.platform import Platform
from levels.spike import Spike
from enemy import Enemy


class Level2(Level):
    def setup_level(self):
        self.chapter_number = "Chapter 2"
        
        self.platforms.add(Platform(0, 0, 40, 600),
                            Platform(0, 0, 1200, 40),
                            Platform(1160, 0,  40, 600),
                            Platform(0, 700, 1200, 100),
                            Platform(900, 200, 40, 500),
                            Platform(40, 560, 650, 40),
                            Platform(840, 640, 60, 60),
                            Platform(250, 400, 650, 40),
                            Platform(40, 490, 60, 100),
                            Platform(840, 300, 60, 100)
                            )

        self.enemies.add(Enemy(750, 690, [(400, 690), (750, 690)]),
                         Enemy(200, 550, [(200, 550), (600, 550)]),
                         Enemy(400, 400, [(400, 400), (750, 400)])
                         )
        
        self.obstacles.add(Spike(0, 660))