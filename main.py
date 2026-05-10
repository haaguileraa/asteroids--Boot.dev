import pygame 
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
FPS = 60

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt =  0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return           
        
        updatable.update(dt)

        screen.fill("black")
        # add game elements here (after drawing the background) 
        for element in drawable:
            element.draw(screen)
        
        # last step:
        pygame.display.flip() # refresh screen
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
