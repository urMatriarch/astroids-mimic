from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def _init__(self, x, y, radius):
        super().__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        negative_angle = self.velocity.rotate(-rand_angle)
        positive_angle = self.velocity.rotate(rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        negative_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        negative_asteroid.velocity = (negative_angle * 1.2)
        positive_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        positive_asteroid.velocity = (positive_angle * 1.2)