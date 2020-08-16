import pygame
import math
from nodes import *
from queue import PriorityQueue


# Define Display settings
WIDTH = 800
ROWS = 40
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Visualizer")


# Main function
def main(win, width, ROWS):
    grid = make_grid(ROWS, width)

    # Start/end nodes booleans
    start = None
    end = None
    
    # Program running booleans
    run = True
    started = False

    # Running program loop
    while run:
        # Draw elements to the display
        draw(win, grid, ROWS, width)

        # Check for events
        for event in pygame.event.get():
            # Check for quit
            if event.type == pygame.QUIT:
                run = False
                       
            # Check left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_blocked()

            
            # Check right mouse click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None
            
            # Start the visualizer
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    
    pygame.quit()


# H(n) function (heuristic)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Function to draw shortest_path
def shortest_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


# A* search algorithm
def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_value = {node: float("inf") for row in grid for node in row}
    g_value[start] = 0

    f_value = {node: float("inf") for row in grid for node in row}
    f_value[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            shortest_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            temp_g_value = g_value[current] + 1
            
            if temp_g_value < g_value[neighbor]:
                came_from[neighbor] = current
                g_value[neighbor] = temp_g_value
                f_value[neighbor] = temp_g_value + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_value[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()

        if current != start:
            current.make_visited()

    return False


# Definition of Grid
def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid


# Draw Grid
def draw_grid(win, rows, width):
    gap = width // rows
    
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# Def draw of display
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


# Function to get mouse position
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap

    return row, col


if __name__ == "__main__":
    main(WINDOW, WIDTH, ROWS)
