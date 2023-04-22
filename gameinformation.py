import pygame
import math

# Colors
white = (255, 255, 255)
black = (0, 0, 0)


class GameInformation:
    def __init__(self, base_x, width, base_width, base_acceleration, pendulum_angle, pendulum_angular_velocity, key_left, key_right):
        self.base_x = base_x
        self.base_acceleration = base_acceleration
        self.pendulum_angle = pendulum_angle
        self.pendulum_angular_velocity = pendulum_angular_velocity
        self.key_left = key_left
        self.key_right = key_right
        self.normalized_base_speed = self.return_normalized_base_speed(base_acceleration, 10)
        self.normalized_base_x = self.return_normalized_base_x(base_x, width, base_width)
        self.normalized_pendulum_angle, self.normalized_pendulum_angular_velocity = self.normalize_pendulum_angle_and_velocity(pendulum_angle, pendulum_angular_velocity)

    @staticmethod
    def return_normalized_base_x(base_x, width, base_width):
        normalized_base_x = (base_x / ((width - base_width) / 2)) - 1
        return normalized_base_x

    @staticmethod
    def normalize_pendulum_angle_and_velocity(pendulum_angle, pendulum_angular_velocity):
        pendulum_angle = pendulum_angle * 180 / math.pi
        pendulum_angle = pendulum_angle + 180
        if pendulum_angle > 359:
            pendulum_angle = pendulum_angle - 359

        normalized_pendulum_angle = (pendulum_angle / 180) - 1

        max_angular_velocity = 10  # Define the maximum expected angular velocity here
        normalized_pendulum_angular_velocity = min(max(pendulum_angular_velocity / max_angular_velocity, -1), 1)

        return normalized_pendulum_angle, normalized_pendulum_angular_velocity
    
    def return_normalized_base_speed(self, base_acceleration, max_speed):
        normalized_base_speed = base_acceleration / max_speed
        return normalized_base_speed

    def display_information(self, screen):
        self.display_base_x_position(screen)
        self.display_base_speed(screen)
        self.display_pendulum_angle(screen)
        self.display_pendulum_angular_velocity(screen)
        self.display_input_data(screen)

    def display_base_x_position(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Base X-Position: {self.base_x:.1f} (Normalized: {self.normalized_base_x:.2f})", True, black, white)
        screen.blit(text, (10, 10))

    def display_base_speed(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Base Speed: {self.base_acceleration:.1f}", True, black, white)
        screen.blit(text, (10, 50))

    def normalize_base_speed(base_acceleration, max_speed):
        normalized_base_speed = base_acceleration / max_speed
        return normalized_base_speed

    def display_pendulum_angle(self, screen):
        pendulum_angle_degrees = self.pendulum_angle * 180 / math.pi
        pendulum_angle_degrees = pendulum_angle_degrees + 180
        if pendulum_angle_degrees > 359:
            pendulum_angle_degrees = pendulum_angle_degrees - 359
        font = pygame.font.Font(None, 36)
        text = font.render(f"Pendulum Angle: {pendulum_angle_degrees:.0f} (Normalized: {self.normalized_pendulum_angle:.2f})", True, black, white)
        screen.blit(text, (10, 90))

    def display_pendulum_angular_velocity(self, screen):
        angular_velocity = self.pendulum_angular_velocity * 180 / math.pi
        font = pygame.font.Font(None, 36)
        text = font.render(f"Pendulum Angular Velocity: {angular_velocity:.1f} (Normalized: {self.normalized_pendulum_angular_velocity*12:.2f})", True,black, white)
        screen.blit(text, (10, 130))

    def display_input_data(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Input Data: Left: {self.key_left}, Right: {self.key_right}", True, black, white)
        screen.blit(text, (10, 170))


