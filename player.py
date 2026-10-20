import pygame
from circleshape import CircleShape
from shot import Shot
import constants
from sys import exit

class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0

    def draw(self, screen: object):
        self.screen = screen
        pygame.draw.polygon(
            surface = screen,
            color = "white",
            points = self.triangle(),
            width = constants.LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_cooldown_timer -= dt

    def rotate(self, dt: float) -> float:
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
        return self.rotation

    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_with_speed = constants.PLAYER_SPEED * rotated_vector * dt
        self.position += rotated_vector_with_speed

    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return
        else:
            x, y = self.position
            shot = Shot(x, y, constants.SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity = shot.velocity.rotate(self.rotation)
            shot.velocity *= constants.PLAYER_SHOOT_SPEED
            self.shoot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
