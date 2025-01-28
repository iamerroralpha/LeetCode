import turtle

cell_size = 400  # Size of each grid cell 20
grid_rows = 4  # Number of rows 27
grid_cols = 4  # Number of columns 41
animate_limit = 10  # Number of squares to draw with animation
grid_offset_x = -400  # Starting x position of the grid
grid_offset_y = -400  # Starting y position of the grid

def draw_square(size, offset_x=0, offset_y=0):
    """Draws a square with the given size at the specified offset."""
    turtle.penup()
    turtle.goto(offset_x, offset_y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_bouncy_diagonals(cell_size=20, grid_offset_x=0, grid_offset_y=0):
    """Uses the draw_diagonal_ lines method until it bounces and then changes direction."""
    x, y = grid_offset_x, grid_offset_y

    while x < grid_offset_x + grid_cols * cell_size and y < grid_offset_y + grid_rows * cell_size:
        x, y = draw_diagonal_lines_2(cell_size, 4, x, y)

def draw_diagonal_lines_2(size, spacing, offset_x=0, offset_y=0):
    """Draws diagonal lines at the opposite 45-degree angle  within a square."""
    for i in range(size // spacing + 1):
        # Draw lines parallel to one diagonal
        start_x = offset_x + i * spacing
        start_y = offset_y + size
        end_x = offset_x
        end_y = offset_y + size - i * spacing

        if i * spacing <= size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    for i in range(1, size // spacing + 1):
        # Draw lines parallel to the other diagonal
        start_x = offset_x + i * spacing
        start_y = offset_y
        end_x = offset_x + size
        end_y = offset_y + i * spacing

        if i * spacing <= size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    current_x = offset_x + size
    current_y = offset_y + size
    return current_x, current_y


def draw_diagonal_lines_1(size, spacing, offset_x=0, offset_y=0):
    """Draws diagonal lines at a 45-degree angle within a square."""
    for i in range(size // spacing + 1):
        # Draw lines parallel to one diagonal
        start_x = offset_x + i * spacing
        start_y = offset_y
        end_x = offset_x
        end_y = offset_y + i * spacing

        if i * spacing <= size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    for i in range(1, size // spacing + 1):
        # Draw lines parallel to the other diagonal
        start_x = offset_x + size
        start_y = offset_y + i * spacing
        end_x = offset_x + i * spacing
        end_y = offset_y + size

        if i * spacing <= size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)
    current_x = offset_x + size
    current_y = offset_y + size
    return current_x, current_y

def draw_grid(rows, cols, cell_size, animate_limit=None, grid_offset_x=0, grid_offset_y=0):
    """Draws a grid with the specified number of rows and columns."""
    counter = 0
    for row in range(rows):
        for col in range(cols):
            current_x = grid_offset_x + col * cell_size
            current_y = grid_offset_y + row * cell_size

            if animate_limit is not None and counter < animate_limit:
                # Animate drawing for the first few squares
                draw_square(cell_size, current_x, current_y)
                counter += 1
            elif animate_limit is not None and counter == animate_limit:
                # Draw the rest of the grid in the background
                for r in range(row, rows):
                    for c in range(col if r == row else 0, cols):
                        draw_square(cell_size, grid_offset_x + c * cell_size, grid_offset_y + r * cell_size)
                return

# Main script setup
def main():
    turtle.screensize(canvwidth=1000, canvheight=1000)
    turtle.speed(600)  # Moderate animation speed for the first few squares

    turtle.tracer(0, 0)  # Disable animation for fast rendering
    # Draw the grid
    turtle.color("black")
    draw_grid(grid_rows, grid_cols, cell_size, animate_limit, grid_offset_x, grid_offset_y)

    turtle.tracer(1, 0)  # Re-enable animation
    # Draw diagonal lines in the first cell
    draw_bouncy_diagonals(cell_size=cell_size, grid_offset_x=grid_offset_x, grid_offset_y=grid_offset_y)
    # Finish drawing
    turtle.done()

if __name__ == "__main__":
    main()
