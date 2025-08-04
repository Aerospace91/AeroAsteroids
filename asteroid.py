import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #Splitting Asteroids
        random_angle = random.uniform(20, 50)
        rand_one = self.velocity.rotate(random_angle)
        rand_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_one.velocity = rand_one * 1.2
        new_ast_two.velocity = rand_two * 1.2