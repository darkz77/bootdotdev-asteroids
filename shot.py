import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y:float, radius: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: object):
        self.screen = screen
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = SHOT_RADIUS,
            width = LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
