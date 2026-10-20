from random import uniform

import pygame
from circleshape import CircleShape
import constants
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: object):
        self.screen = screen
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = self.radius,
            width = constants.LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(angle)
            new_velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            x, y = self.position
            new_asteroid_1 = Asteroid(x, y, new_radius)
            new_asteroid_1.velocity = new_velocity_1 * 1.2
            new_asteroid_2 = Asteroid(x, y, new_radius)
            new_asteroid_2.velocity = new_velocity_2 * 1.2
