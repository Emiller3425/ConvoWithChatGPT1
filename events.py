import pygame
from buttons import Button

def handle_events(event, calculator, operation_buttons, number_buttons, equals_button, clear_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            pos = pygame.mouse.get_pos()

            # Check if any operation button was clicked
            for label, button_func in operation_buttons.items():
                if button_func is not None:
                    if button_func(label) is not None and button_func(label).check_click(pos):
                        calculator.handle_input(label)
                        return  # Exit the function after handling the click

            # Check if any number button was clicked
            for num_button in number_buttons:
                if num_button.check_click(pos):
                    calculator.handle_input(num_button.label)
                    return  # Exit the function after handling the click

            # Check if the '=' button was clicked
            if equals_button.check_click(pos):
                calculator.handle_input("=")
                return  # Exit the function after handling the click

            # Check if the 'Clear' button was clicked
            if clear_button.check_click(pos):
                calculator.handle_input("C")

    # If no operation button was clicked, check for other buttons (e.g., numbers)
    # Implement this part according to your button structure

    # Example code for handling number buttons
    # for num_button in number_buttons:
    #     if num_button.check_click(pos):
    #         calculator.handle_input(num_button.label)
    #         return