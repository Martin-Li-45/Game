from levels.level import Level
from levels.platform import Platform
from boss import Boss


class Level3(Level):
    def setup_level(self):
        self.chapter_number = "Chapter 3"
        
        self.platforms.add(Platform(0, 0, 40, 600),
                            Platform(0, 0, 1200, 40),
                            Platform(1160, 0,  40, 800),
                            Platform(0, 700, 1200, 100),
                            Platform(0, 600, 100, 20))
        
        self.bosses.add(Boss(900, 690, [(300, 690), (900, 690)]))
  