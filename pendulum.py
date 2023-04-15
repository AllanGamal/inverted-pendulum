import pygame
import math
import displayData

pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Pendulum parameters
pendulum_length = 150
pendulum_mass = 10
pendulum_angle = math.pi / 4
pendulum_angular_velocity = 0

# Constants
gravity = 9.81
delta_t = 0.2

# Base parameters
base_width = 40
base_height = 20
base_speed = 5
base_x = (width - base_width) / 2
base_y = height - base_height - pendulum_length

damper = 0.995

def calculate_damper(speed):
    # Define the relationship between speed and damper here
    if speed <= 0.025:
        return 0.95
    elif speed <= 0.05:
        return 0.98
    return 0.995

def draw_base(x, y):
    pygame.draw.rect(screen, black, (x, y, base_width, base_height))

def draw_pendulum(x, y, angle):
    end_x = x + pendulum_length * math.sin(angle)
    end_y = y - pendulum_length * math.cos(angle)
    pygame.draw.line(screen, black, (x, y), (end_x, end_y), 2)
    pygame.draw.circle(screen, black, (int(end_x), int(end_y)), pendulum_mass)


def main():
    global base_x, pendulum_angle, pendulum_angular_velocity, base_speed
    clock = pygame.time.Clock()
    running = True
    key_left = False
    key_right = False
    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        base_acceleration = 0
        if keys[pygame.K_LEFT]:
            base_acceleration = -base_speed
            key_left = True
        else:
            key_left = False
        if keys[pygame.K_RIGHT]:
            base_acceleration = base_speed
            key_right = True
        else:
            key_right = False

        if base_x == 0 and base_acceleration < 0:
            base_speed = 0
        elif base_x == width - base_width and base_acceleration > 0:
            base_speed = 0
        else:
            base_speed = 5

        base_x += base_acceleration
        base_x = max(min(base_x, width - base_width), 0)

        # Compute acceleration due to gravity and horizontal acceleration
        pendulum_gravity_acceleration = (gravity / pendulum_length) * math.sin(pendulum_angle)
        pendulum_horizontal_acceleration = -base_acceleration * math.cos(pendulum_angle) / pendulum_length

        # Update angular velocity and angle
        pendulum_angular_velocity += (pendulum_gravity_acceleration + pendulum_horizontal_acceleration) * delta_t
        pendulum_angular_velocity *= calculate_damper(abs(pendulum_angular_velocity))
        pendulum_angle += pendulum_angular_velocity * delta_t
        

        ## make the angle between 0 and 360 degrees, 180 degrees is the vertical position (upwards)
        pendulum_angle = pendulum_angle % (2 * math.pi)
        






        draw_base(base_x, base_y)
        draw_pendulum(base_x + base_width / 2, base_y, pendulum_angle)
        # In pendulum.py
        displayData.display_base_x_position(screen, base_x, width, base_width)  # Add base_width as an argument
        displayData.display_base_speed(screen, base_acceleration/5)  # Change the argument
        displayData.display_pendulum_angle(screen, pendulum_angle)
        displayData.display_pendulum_angular_velocity(screen, pendulum_angular_velocity)
        displayData.display_input_data(screen, key_left, key_right)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

