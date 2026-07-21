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
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        ran = random.uniform(20, 50)
        ast1 = self.velocity.rotate(ran)
        ast2 = self.velocity.rotate(-ran)
        ast_r = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, ast_r)
        new_ast2 = Asteroid(self.position.x, self.position.y, ast_r)
        new_ast1.velocity *= ast1 * 1.2
        new_ast1.velocity *= ast2 * 1.2