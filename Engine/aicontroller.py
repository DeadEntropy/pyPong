from enum import Enum
from movement import Velocity
import sdl2.ext

class TrackingAIController(sdl2.ext.Applicator):
    def __init__(self, miny, maxy):
        super(TrackingAIController, self).__init__()
        self.componenttypes = PlayerData, Velocity, sdl2.ext.Sprite
        self.miny = miny
        self.maxy = maxy
        self.ball = None

    def process(self, world, componentsets):
        print(f"Process - {type(self).__name__}")
        for pdata, vel, sprite in componentsets:
            if not pdata.ai:
                continue

            centery = sprite.y + sprite.size[1] // 2
            if (self.ball.velocity.vx < 0 and pdata.side == Side.RIGHT) or  (self.ball.velocity.vx > 0 and pdata.side == Side.LEFT):
                # ball is moving away from the AI
                if centery < self.maxy // 2:
                    vel.vy = 3
                elif centery > self.maxy // 2:
                    vel.vy = -3
                else:
                    vel.vy = 0
            else:
                bcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
                if bcentery < centery - 1:
                    vel.vy = -3
                elif bcentery > centery + 1:
                    vel.vy = 3
                else:
                    vel.vy = 0

class Side(Enum):
    LEFT = 0
    RIGHT = 1

class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.ai = False
        self.side = Side.LEFT