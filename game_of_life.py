import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Initialize the pygame module
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.2, 0.8])

# Define the colors for alive and dead cells
colors = {0: WHITE, 1: BLACK}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a copy of the grid to update without modifying the original
    new_grid = grid.copy()

    # Update the grid based on the rules of Conway's Game of Life
    for i in range(ROWS):
        for j in range(COLS):
            total = np.sum(grid[max(0, i-1):min(ROWS, i+2), max(0, j-1):min(COLS, j+2)]) - grid[i, j]
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    # Update the display based on the new grid
    screen.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(screen, colors[new_grid[i, j]], (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the grid
    grid = new_grid.copy()

    # Update the display
    pygame.display.flip()

    # Add a small delay
    pygame.time.delay(100)

pygame.quit()
