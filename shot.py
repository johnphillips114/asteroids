from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = self.radius,
            width = 2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)