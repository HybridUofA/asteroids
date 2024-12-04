from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randAngle = random.uniform(20, 50)
            leftVelocity = self.velocity.rotate(-randAngle)
            rightVelocity = self.velocity.rotate(randAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            leftAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
            rightAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
            leftAsteroid.velocity = leftVelocity * 1.2
            rightAsteroid.velocity = rightVelocity * 1.2