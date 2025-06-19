from levels.level import Level
from levels.platform import Platform
from levels.spike import Spike
from levels.puzzle import PuzzleTrigger


class Level1(Level):
    def setup_level(self):
        self.chapter_number = "Chapter 1"
        
        self.platforms.add(Platform(0, 0, 40, 800),
                            Platform(0, 0, 1200, 40),
                            Platform(1160, 0,  40, 600),
                            Platform(0, 700, 1200, 100),
                            Platform(550, 200, 40, 500),
                            Platform(400, 600, 150, 40),
                            Platform(40, 500, 150, 40),
                            Platform(400, 400, 150, 40),
                            Platform(40, 300, 150, 40),
                            Platform(400, 200, 150, 40),
                            Platform(590, 250, 400, 40),
                            Platform(760, 500, 400, 40)
                            )
        
        self.spikes.add(Spike(590, 210),
                        Spike(630, 210),
                        Spike(670, 210),
                        Spike(710, 210),
                        Spike(760, 460),
                        Spike(800, 460),
                        Spike(840, 460),
                        Spike(880, 460),
                        Spike(920, 460),
                        )
        
        self.obstacles.add(Spike(1160, 660))
        
        self.puzzle_triggers.add(PuzzleTrigger(1050, 620))
     


        