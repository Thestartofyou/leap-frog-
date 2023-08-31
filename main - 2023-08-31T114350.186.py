import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Frog properties
frog_width = 50
frog_height = 50
frog_x = SCREEN_WIDTH // 2 - frog_width // 2
frog_y = SCREEN_HEIGHT - frog_height - 10
frog_speed = 5

# Car properties
car_width = 100
car_height = 50
car_x = random.randint(0, SCREEN_WIDTH - car_width)
car_y = frog_y - car_height
car_speed = 3

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Leap Frog Game")
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and frog_x > 0:
        frog_x -= frog_speed
    if keys[pygame.K_RIGHT] and frog_x < SCREEN_WIDTH - frog_width:
        frog_x += frog_speed

    car_x += car_speed
    if car_x > SCREEN_WIDTH:
        car_x = -car_width
        car_y = frog_y - car_height
        car_speed = random.randint(3, 8)

    # Check for collision
    if frog_x + frog_width > car_x and frog_x < car_x + car_width and frog_y == car_y:
        game_over = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (frog_x, frog_y, frog_width, frog_height))
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

