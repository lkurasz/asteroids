import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    color = (0,0,0)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for a in asteroids:
            colide = a.collisions(player)
            if colide:
                print("Game over!")
                sys.exit()

        screen.fill(color)
        
        for o in drawable:
            o.draw(screen)
          
        pygame.display.flip()

        value = clock.tick(60)
        dt = value/1000
        

if __name__ == "__main__":
    main()
