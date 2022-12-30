import sys
import sdl2
import sdl2.ext
import constants as cst
import movement as mov
import collision as col
import entities as ent
import aicontroller as aic
import scorecounter as scc

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, cst.BLACK)
        super(SoftwareRenderer, self).render(components)

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window(cst.GAME_NAME, size=(cst.WINDOW_WIDTH, cst.WINDOW_HEIGHT))
    window.show()

    renderer = sdl2.ext.Renderer(window)

    world = sdl2.ext.World()
    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    sdl2.ext.FontManager(font_path = ".\Asset\OpenSans-Regular.ttf", size = 14, color=cst.WHITE)

    movement = mov.MovementSystem(0, 0, cst.WINDOW_WIDTH, cst.WINDOW_HEIGHT)
    collision = col.CollisionSystem(0, 0, cst.WINDOW_WIDTH, cst.WINDOW_HEIGHT)
    spriterenderer = factory.create_sprite_render_system()
    
    aicontroller = aic.TrackingAIController(0, cst.WINDOW_HEIGHT)
    score_counter_system = scc.ScoreCounterSystem(0, cst.WINDOW_WIDTH)
    
    world.add_system(aicontroller)
    world.add_system(movement)
    world.add_system(score_counter_system)
    world.add_system(collision)
    world.add_system(spriterenderer)

    sp_ball = factory.from_color(cst.WHITE, size=(cst.PADDLE_WIDTH, cst.PADDLE_WIDTH))
    sp_paddle1 = factory.from_color(cst.WHITE, size=(cst.PADDLE_WIDTH, cst.PADDLE_HEIGHT))
    sp_paddle2 = factory.from_color(cst.WHITE, size=(cst.PADDLE_WIDTH, cst.PADDLE_HEIGHT))

    ball = ent.Ball(world, sp_ball, (cst.WINDOW_WIDTH - cst.PADDLE_WIDTH)//2, (cst.WINDOW_HEIGHT - cst.PADDLE_WIDTH)//2)
    ball.velocity.vx = -3
    ball.velocity.vy = -1

    paddle_start_height = (cst.WINDOW_HEIGHT - cst.PADDLE_HEIGHT)//2
    player1 = ent.Player(world, sp_paddle1, 0, paddle_start_height, False)
    player2 = ent.Player(world, sp_paddle2, cst.WINDOW_WIDTH - cst.PADDLE_WIDTH, paddle_start_height, True)

    score_board = ent.ScoreBoard(world, cst.WINDOW_WIDTH//2, 50, renderer=renderer)


    collision.ball = ball
    aicontroller.ball = ball
    score_counter_system.ball = ball

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if not player1.playerdata.ai and event.key.keysym.sym == sdl2.SDLK_UP:
                    player1.velocity.vy = -3
                elif not player1.playerdata.ai and event.key.keysym.sym == sdl2.SDLK_DOWN:
                    player1.velocity.vy = 3
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_DOWN):
                    player1.velocity.vy = 0
        sdl2.SDL_Delay(10)
        renderer.clear()
        print('Process World')
        world.process()

if __name__ == "__main__":
    sys.exit(run())