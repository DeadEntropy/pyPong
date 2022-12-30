import sdl2.ext
import constants as cst

class ScoreCounterSystem(sdl2.ext.Applicator):
    def __init__(self, minx, maxx):
        super().__init__()
        self.componenttypes = (ScoreCounter, sdl2.ext.Sprite)
        self.ball = None
        self.minx = minx
        self.maxx = maxx

    def process(self, world, componentsets):
        print(f"Process - {type(self).__name__}")
        for score_counter, textsprite in componentsets:
            # if the ball touches left or right wall update the counter
            if self.ball.sprite.x <= self.minx + cst.PADDLE_WIDTH // 2:
                score_counter.right_player = score_counter.right_player + 1
            elif self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx - cst.PADDLE_WIDTH // 2:
                score_counter.left_player = score_counter.left_player + 1
            
            textsprite.text = f"{score_counter.left_player} - {score_counter.right_player}"


class ScoreCounter(object):
    def __init__(self):
        super().__init__()

        self.left_player = 0
        self.right_player = 0