import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        
        ran = random.uniform(20, 50)
        
        a = self.velocity.rotate(ran)
        b = self.velocity.rotate(-ran)
        
        new_r = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_r)
        asteroid.velocity = a * 1.2
        
        asteroid = Asteroid(self.position.x, self.position.y, new_r)
        asteroid.velocity = b * 1.2