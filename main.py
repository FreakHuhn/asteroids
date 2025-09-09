import pygame
from constants import *
from player import * 
from circleshape import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Shot.containers = (updatable, drawable, shots)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        asteroids.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        for sprite in asteroids:
            if player.check_collision(sprite):
                print("Game Over!")
                raise SystemExit
            for shot in shots:
                if shot.check_collision(sprite):
                    shot.kill()
                    sprite.split()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()