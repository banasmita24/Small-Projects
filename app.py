import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 700
HEIGHT = 600
ROWS = 6
COLS = 7
SQUARE_SIZE = 100

# Set up some colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game board
board = np.zeros((ROWS, COLS))

# Set up the AI
class Connect4AI:
    def __init__(self):
        self.weights = np.random.rand(ROWS * COLS, COLS)

    def train(self, X, y):
        for x, y in zip(X, y):
            self.weights += np.outer(x, y)

    def predict(self, board):
        return np.argmax(np.dot(board.flatten(), self.weights))

ai = Connect4AI()

# Train the AI on a dataset of Connect4 games
# For this example, we'll just generate some random data
X = np.random.rand(100, ROWS * COLS)
y = np.random.randint(0, COLS, 100)
ai.train(X, y)

# Set up the game loop
def check_win(board, player):
    # Check rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row, col] == player and board[row, col + 1] == player and board[row, col + 2] == player and board[row, col + 3] == player:
                return True

    # Check columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row, col] == player and board[row + 1, col] == player and board[row + 2, col] == player and board[row + 3, col] == player:
                return True

    # Check diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row, col] == player and board[row + 1, col + 1] == player and board[row + 2, col + 2] == player and board[row + 3, col + 3] == player:
                return True
            if board[row, col + 3] == player and board[row + 1, col + 2] == player and board[row + 2, col + 1] == player and board[row + 3, col] == player:
                return True

    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column where the user clicked
            col = event.pos[0] // SQUARE_SIZE
            # Get the row where the user clicked
            row = event.pos[1] // SQUARE_SIZE
            # Check if the move is valid
            if board[row, col] == 0:
                # Make the move
                board[row, col] = 1
                # Check if the game is won
                if check_win(board, 1):
                    print("Player 1 wins!")
                    pygame.quit()
                    sys.exit()
                # Make the AI move
                ai_move = ai.predict(board)
                for row in range(ROWS - 1, -1, -1):
                    if board[row, ai_move] == 0:
                        board[row, ai_move] = 2
                        break
                # Check if the game is won
                if check_win(board, 2):
                    print("Player 2 wins!")
                    pygame.quit()
                    sys.exit()

    # Draw the game board
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, RED if board[row, col] == 1 else YELLOW if board[row, col] == 2 else BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    # Update the display
    pygame.display.flip()