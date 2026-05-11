import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state, log_event
from shot import Shot


FPS = 60

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt =  0

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidField = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Shot.containers = (shots, updatable, drawable)

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return           
        
        updatable.update(dt)

        for asteroid in asteroids:
            # let's first check if the player was hit
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # now shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")
        # add game elements here (after drawing the background) 
        for element in drawable:
            element.draw(screen)
        
        # last step:
        pygame.display.flip() # refresh screen
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
