import movement as mov
import scorecounter as scc
import aicontroller
from Others.textsprite import TextSprite
import sdl2.ext

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0, ai=False):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = mov.Velocity()
        self.playerdata = aicontroller.PlayerData()
        self.playerdata.ai = ai
        self.playerdata.side = aicontroller.Side.LEFT if posx == 0 else aicontroller.Side.RIGHT


class Ball(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.velocity = mov.Velocity()


class ScoreBoard(sdl2.ext.Entity):
    def __init__(self, world, posx, posy, renderer):        
        self.sprite = TextSprite(renderer, text="0 - 0")
        self.sprite.position = posx, posy
        #self.textsprite.x = posx
        #self.textsprite.y = posy
        self.scorecounter = scc.ScoreCounter()
        self.scorecounter.left_player = 0
        self.scorecounter.right_player = 0