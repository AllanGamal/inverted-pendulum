import pygame
import math
from gameinformation import GameInformation
# Colors
white = (255, 255, 255)
black = (0, 0, 0)

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

        self.pendulum_length = 150
        self.pendulum_mass = 10
        self.pendulum_angle = math.pi / 4
        self.pendulum_angular_velocity = 0
        self.gravity = 9.81
        self.delta_t = 0.2
        self.base_width = 40
        self.base_height = 20
        self.base_speed = 5
        self.base_x = (width - self.base_width) / 2
        self.base_y = height - self.base_height - self.pendulum_length
        self.damper = 0.995

    def calculate_damper(self, speed):
        if speed <= 0.025:
            return 0.95
        elif speed <= 0.05:
            return 0.98
        return 0.995

    def draw_base(self, x, y):
        pygame.draw.rect(self.screen, black, (x, y, self.base_width, self.base_height))

    def draw_pendulum(self, x, y, angle):
        end_x = x + self.pendulum_length * math.sin(angle)
        end_y = y - self.pendulum_length * math.cos(angle)
        pygame.draw.line(self.screen, black, (x, y), (end_x, end_y), 2)
        pygame.draw.circle(self.screen, black, (int(end_x), int(end_y)), self.pendulum_mass)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        key_left = False
        key_right = False

        while running:
            self.screen.fill(white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            base_acceleration = 0
            if keys[pygame.K_LEFT] and self.base_x > 0:
                base_acceleration = -self.base_speed
                key_left = True
            else:
                key_left = False
            if keys[pygame.K_RIGHT] and self.base_x < self.width - self.base_width:
                base_acceleration = self.base_speed
                key_right = True
            else:
                key_right = False

            if self.base_x == 0 and base_acceleration < 0:
                self.base_speed = 0
            elif self.base_x == self.width - self.base_width and base_acceleration > 0:
                self.base_speed = 0
            else:
                self.base_speed = 5

            self.base_x += base_acceleration
            self.base_x = max(min(self.base_x, self.width - self.base_width), 0)

            pendulum_gravity_acceleration = (self.gravity / self.pendulum_length) * math.sin(self.pendulum_angle)
            pendulum_horizontal_acceleration = -base_acceleration * math.cos(self.pendulum_angle) / self.pendulum_length

            self.pendulum_angular_velocity += (pendulum_gravity_acceleration + pendulum_horizontal_acceleration) * self.delta_t
            self.pendulum_angular_velocity *= self.calculate_damper(abs(self.pendulum_angular_velocity))
            self.pendulum_angle += self.pendulum_angular_velocity * self.delta_t

            self.pendulum_angle = self.pendulum_angle % (2 * math.pi)

            self.draw_base(self.base_x, self.base_y)
            self.draw_pendulum(self.base_x + self.base_width / 2, self.base_y, self.pendulum_angle)

            game_information = GameInformation(self.base_x, self.width, self.base_width, base_acceleration, self.pendulum_angle, self.pendulum_angular_velocity, key_left, key_right)
            game_information.display_information(self.screen)

            pygame.display.flip()
            clock.tick(60)