import pygame 
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return            
        screen.fill("black")
        # last step:
        pygame.display.flip() # refresh screen


if __name__ == "__main__":
    main()
