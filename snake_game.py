import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Snake block size and speed
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Fonts
FONT_STYLE = pygame.font.SysFont(None, 50)
SCORE_FONT = pygame.font.SysFont(None, 35)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


# Function to display the score on the screen
def display_score(score):
    value = SCORE_FONT.render("Your Score: " + str(score), True, WHITE)
    window.blit(value, [10, 10])


# Function to draw the snake on the window
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, BLACK, [x[0], x[1], snake_block, snake_block])


# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Snake initial position
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Snake initial movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Initial food position
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(BLUE)
            message = FONT_STYLE.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            window.blit(message, [WIDTH / 6, HEIGHT / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Wait for player input to quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Capture player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change
        window.fill(BLUE)
        pygame.draw.rect(window, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove the tail of the snake if it gets too long
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and the food on the window
        draw_snake(BLOCK_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        # Set the game speed
        clock.tick(SNAKE_SPEED)

    pygame.quit()


# Run the game loop
game_loop()
