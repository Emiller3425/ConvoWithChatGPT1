import pygame
from constants import BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_FONT_SIZE

class Button:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        self.is_clicked = False  # Initially, the button is not clicked

    def draw(self, screen):
        # Draw the button rectangle
        if self.is_clicked:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Highlight when clicked
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, self.rect)

        # Draw the button label
        text = self.font.render(self.label, True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.is_clicked = True  # Set the button as clicked
            return True
        else:
            self.is_clicked = False  # Set the button as not clicked
            return False

    def unclick(self):
        self.is_clicked = False  # Manually unclick the button

    def is_clicked(self):
        return self.is_clicked  # Check if the button is currently clicke