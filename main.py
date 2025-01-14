import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from score import Score
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    current_num_lives = PLAYER_LIVES
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score = Score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")
        score.update(dt)

        for member in updatable:
            member.update(dt)
        for member in drawable:
            member.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    score.add_score(ASTEROID_POINT_VALUE)
                    asteroid.split()
                    
            if asteroid.check_collision(player):
                current_num_lives -= 1
                for living_asteroid in asteroids:
                    living_asteroid.kill()
                player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            
            if current_num_lives <= 0:
                print("Game over!")
                print(f"Final score: {int(score.score)}")
                return

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()