import pygame

# Colors
WHITE = (255, 255, 255)  # Background
BLACK = (0, 0, 0)  # Barriers
RED =  (224, 108, 117) # Visited nodes
GREEN = (152, 195, 121) # Shortest path
YELLOW = (229, 192, 123) # Open node
PURPLE = (198, 120, 221) # Start Node
GREY = (92, 99, 112) # Grid
TURQUOISE = (86, 182, 194) # Final Node


class Node:
    """Properties and function of the nodes"""
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Gets node position
    def get_pos(self):
        return self.row, self.col

    # Returns if the node was already visited
    def is_visited(self):
        return self.color == RED
    
    # Returns if the node was not yet visited
    def is_open(self):
        return self.color == YELLOW

    # Returns if the node is a barrier
    def is_blocked(self):
        return self.color == BLACK
    
    # Return if the node is the start node
    def is_start(self):
        return self.color == PURPLE

    # Return if the node is end node
    def is_end(self):
        return self.color == TURQUOISE

    # Reset
    def reset(self):
        self.color = WHITE
    
    # Turns the node the start node
    def make_start(self):
        self.color = PURPLE

    # Turns the node visited
    def make_visited(self):
        self.color = RED

    # Turns the node open
    def make_open(self):
        self.color = YELLOW
    
    # Turns the node into a barrier
    def make_blocked(self):
        self.color = BLACK
    
    # Turns the node the end node
    def make_end(self):
        self.color = TURQUOISE
    
    # Turns the node a part of the shortest path
    def make_path(self):
        self.color = GREEN
    
    # Function to draw the node in the display window
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        # Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_blocked():
            self.neighbors.append(grid[self.row + 1][self.col])
        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked():
            self.neighbors.append(grid[self.row - 1][self.col])
        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_blocked():
            self.neighbors.append(grid[self.row][self.col + 1])
        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_blocked():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
