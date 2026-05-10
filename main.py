import pygame 
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

FPS = 60

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt =  0
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return            
        screen.fill("black")
        # last step:
        pygame.display.flip() # refresh screen
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
