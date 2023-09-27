import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from events import handle_events
from display import draw_screen, draw_button
from calculator import Calculator
from buttons import Button

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Calculator App")

# Create a calculator instance
calculator = Calculator()

# Create buttons for addition, subtraction, multiplication, and division
add_button = Button(50, 200, 100, 50, "+")
subtract_button = Button(50, 260, 100, 50, "-")
multiply_button = Button(50, 320, 100, 50, "*")
divide_button = Button(50, 380, 100, 50, "/")
clear_button = Button(235, 395, 60, 60, "C")
square_root_button = Button(50, 500, 100, 50, "√")
square_button = Button(50, 440, 100, 50, "^2")
equals_button = Button(315, 500, 50, 50, "=")
open_parentheses_button = Button(170, 500, 50, 50, "(")
close_parentheses_button = Button(230, 500, 50, 50, ")")

# Create number buttons (0-9) in a 3x3 grid
number_buttons = []
button_width = 60
button_height = 60
button_x = 170  # Adjust the starting X position
button_y = 200  # Set the Y position to match the '+' button

for i in range(1, 10):  # Start from 1 to exclude 0
    number_buttons.append(Button(button_x, button_y, button_width, button_height, str(i)))
    button_x += button_width + 5  # Add 5 pixels in between buttons
    if (i - 1) % 3 == 2:  # Start a new row after every 3 numbers
        button_x = 170
        button_y += button_height + 5  # Add 5 pixels for vertical spacing

# Create a dictionary to map button labels to their corresponding functions
operation_buttons = {
    "+": calculator.handle_input,
    "-": calculator.handle_input,
    "*": calculator.handle_input,
    "/": calculator.handle_input,
    "^2": calculator.handle_input,  # Add "^2"
    "√": calculator.handle_input,   # Add "√"
    "(": calculator.handle_input,   # Add "(" for opening parenthesis
    ")": calculator.handle_input    # Add ")" for closing parenthesis
}

# Add the new buttons to the all_buttons list
all_buttons = [add_button, subtract_button, multiply_button, divide_button, square_root_button, square_button, open_parentheses_button, close_parentheses_button] + number_buttons + [equals_button] + [clear_button]


# Game loop
running = True
# Inside the game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            pos = pygame.mouse.get_pos()
            for button in all_buttons:
                if button.rect.collidepoint(pos):
                    input_value = button.label
                    calculator.handle_input(input_value)
    # Update the display
    screen.fill(BACKGROUND_COLOR)
    draw_screen(screen, calculator)
    for button in all_buttons:
        draw_button(screen, button)

    # Refresh the display
    pygame.display.flip()

# Clean up and exit
pygame.quit()