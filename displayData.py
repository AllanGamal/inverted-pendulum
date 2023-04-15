import pygame
import math

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

##### Pendulum base-x position
def return_normalized_base_x(base_x, width, base_width):
    normalized_base_x = (base_x / ((width - base_width) / 2)) - 1
    return normalized_base_x

def display_base_x_position(screen, base_x, width, base_width):
    normalized_base_x = return_normalized_base_x(base_x, width, base_width)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Base X-Position: {base_x:.1f} (Normalized: {normalized_base_x:.2f})", True, black, white)
    screen.blit(text, (10, 10))

##### Pendulum base speed
def display_base_speed(screen, base_acceleration):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Base Speed: {base_acceleration:.1f}", True, black, white)
    screen.blit(text, (10, 50))

##### Pendulum angle
def normalize_pendulum_angle(pendulum_angle):
    pendulum_angle = pendulum_angle * 180 / math.pi
    pendulum_angle = pendulum_angle + 180
    if pendulum_angle > 359:
        pendulum_angle = pendulum_angle - 359

    normalized_pendulum_angle = (pendulum_angle / 180) - 1
    return pendulum_angle, normalized_pendulum_angle

def display_pendulum_angle(screen, pendulum_angle):
    pendulum_angle, normalized_pendulum_angle = normalize_pendulum_angle(pendulum_angle)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Pendulum Angle: {pendulum_angle:.0f} (Normalized: {normalized_pendulum_angle:.2f})", True, black, white)
    screen.blit(text, (10, 90))


##### Pendulum angular velocity
def normalize_pendulum_angular_velocity(pendulum_angular_velocity):
    max_angular_velocity = 10  # Define the maximum expected angular velocity here
    normalized_pendulum_angular_velocity = min(max(pendulum_angular_velocity / max_angular_velocity, -1), 1)
    return pendulum_angular_velocity * 180 / math.pi, normalized_pendulum_angular_velocity

def display_pendulum_angular_velocity(screen, pendulum_angular_velocity):
    angular_velocity, normalized_pendulum_angular_velocity = normalize_pendulum_angular_velocity(pendulum_angular_velocity)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Pendulum Angular Velocity: {angular_velocity:.1f} (Normalized: {normalized_pendulum_angular_velocity*12:.2f})", True, black, white)
    screen.blit(text, (10, 130))

def display_input_data(screen, key_left, key_right):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Input Data: Left: {key_left}, Right: {key_right}", True, black, white)
    screen.blit(text, (10, 170))