import turtle

cell_size = 30  # Size of each grid cell 20
grid_rows =4   # Number of rows 27
grid_cols = 3  # Number of columns 41
animate_limit = 10  # Number of squares to draw with animation
grid_offset_x = -400  # Starting x position of the grid
grid_offset_y = -400  # Starting y position of the grida
azure_spacing = 2

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
    direction_x = 1
    direction_y = 1

    #while x < grid_offset_x + grid_cols * cell_size and y < grid_offset_y + grid_rows * cell_size:
    while True:
        if x >= grid_offset_x + grid_cols * cell_size:
            print(f"change in x")
            direction_x = -direction_x
            x += -cell_size
        elif x < grid_offset_x:
            print(f"change in x")
            direction_x = -direction_x
            x += cell_size
        if y >= grid_offset_y + grid_rows * cell_size:
            print(f"change in y")
            direction_y = -direction_y
            y += -cell_size
        elif y < grid_offset_y:
            print(f"change in y")
            direction_y = -direction_y
            y += cell_size

        if direction_x == 1 and direction_y == 1:
            turtle.color("red")
            x, y = draw_diagonal_lines_11(cell_size, azure_spacing, x, y)
        elif direction_x == 1 and direction_y == -1:
            turtle.color("blue")
            x, y = draw_diagonal_lines_10(cell_size, azure_spacing, x, y)
        elif direction_x == -1 and direction_y == 1:
            turtle.color("green")
            x,y = draw_diagonal_lines_01(cell_size, azure_spacing, x, y)
        elif direction_x == -1 and direction_y == -1:
            turtle.color("black")
            x, y = draw_diagonal_lines_00(cell_size, azure_spacing, x, y)

def draw_diagonal_lines_00(size, spacing, offset_x=0, offset_y=0):
    """Draws diagonal lines at a 45-degree angle within a square."""
    for i in range(size // spacing + 1):
        # Draw lines parallel to one diagonal
        start_x = offset_x + cell_size - i * spacing
        start_y = offset_y + cell_size
        end_x = offset_x + cell_size
        end_y = offset_y + size - i * spacing

        if start_x <= offset_x + size and end_y <= offset_y + size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    for i in range(1, size // spacing + 1):
        # Draw lines parallel to the other diagonal
        start_x = offset_x
        start_y = offset_y + cell_size - i * spacing
        end_x = offset_x + size - i * spacing
        end_y = offset_y

        if start_y <= offset_y + size and end_x <= offset_x + size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    current_x = offset_x - size
    current_y = offset_y - size
    return current_x, current_y

def draw_diagonal_lines_01(size, spacing, offset_x=0, offset_y=0):
    """Draws diagonal lines at the opposite 45-degree angle  direction within a square."""
    # First set of lines (from left edge to bottom edge)
    for i in range(size // spacing + 1):
        start_x = offset_x + cell_size - i * spacing
        start_y = offset_y
        end_x = offset_x + cell_size
        end_y = offset_y + i * spacing

        if start_x <= offset_x + size and end_y <= offset_y + size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    # Second set of lines (from top edge to right edge)
    for i in range(1, size // spacing + 1):
        start_x = offset_x
        start_y = offset_y + i * spacing
        end_x = offset_x + size - i * spacing
        end_y = offset_y + size

        if start_x >= offset_x and end_y <= offset_y + size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    current_x = offset_x - size
    current_y = offset_y + size
    return current_x, current_y

def draw_diagonal_lines_10(size, spacing, offset_x=0, offset_y=0):
    """Draws diagonal lines at the opposite 45-degree angle  direction within a square."""
    # First set of lines (from left edge to bottom edge)
    for i in range(size // spacing + 1):
        start_x = offset_x + i * spacing
        start_y = offset_y + size
        end_x = offset_x
        end_y = offset_y + size - i * spacing

        if start_x <= offset_x + size and end_y >= offset_y:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    # Second set of lines (from top edge to right edge)
    for i in range(1, size // spacing + 1):
        start_x = offset_x + i * spacing
        start_y = offset_y
        end_x = offset_x + size
        end_y = offset_y + cell_size - i * spacing

        if end_x <= offset_x + size and end_y <= offset_y + size:
            turtle.penup()
            turtle.goto(start_x, start_y)
            turtle.pendown()
            turtle.goto(end_x, end_y)

    current_x = offset_x + size
    current_y = offset_y - size
    return current_x, current_y


def draw_diagonal_lines_11(size, spacing, offset_x=0, offset_y=0):
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
