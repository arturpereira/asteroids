# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    Asteroid.containers = (updateable, drawable, asteroids)
    
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    
    Shot.containers = (updateable, drawable, shots)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updateable:
            u.update(dt)
            
        for a in asteroids:
            if a.detect_collision(player):
                print("Game Over!")
                sys.exit()
            
        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()