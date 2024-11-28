import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]

# Shapes of Tetriminoes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

class Tetrimino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetrimino(random.choice(SHAPES))
        self.next_piece = Tetrimino(random.choice(SHAPES))
        self.score = 0
        self.running = True

    def valid_move(self, piece, dx, dy):
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    x = piece.x + j + dx
                    y = piece.y + i + dy
                    if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or (y >= 0 and self.grid[y][x] != BLACK):
                        return False
        return True

    def lock_piece(self):
        for i, row in enumerate(self.current_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + i][self.current_piece.x + j] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = Tetrimino(random.choice(SHAPES))
        if not self.valid_move(self.current_piece, 0, 0):
            self.running = False

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        cleared = GRID_HEIGHT - len(new_grid)
        self.grid = [[BLACK] * GRID_WIDTH for _ in range(cleared)] + new_grid
        self.score += cleared * 10

    def move(self, dx, dy):
        if self.valid_move(self.current_piece, dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
        elif dy:
            self.lock_piece()

    def rotate(self):
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if not self.valid_move(self.current_piece, 0, 0):
            self.current_piece.shape = old_shape

    def draw_grid(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_piece(self, screen, piece):
        for i, row in enumerate(piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, piece.color, (
                        (piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                    ))
                    pygame.draw.rect(screen, GRAY, (
                        (piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                    ), 1)

    def draw(self, screen):
        screen.fill(BLACK)
        self.draw_grid(screen)
        self.draw_piece(screen, self.current_piece)
        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    game = Tetris()

    # Timing variables
    fall_time = 0
    fall_speed = 500  # Milliseconds per block fall

    while game.running:
        screen.fill(BLACK)
        game.draw(screen)
        dt = clock.tick(30)
        fall_time += dt

        # Piece falls every `fall_speed` milliseconds
        if fall_time > fall_speed:
            game.move(0, 1)
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

    pygame.quit()

if __name__ == "__main__":
    main()
