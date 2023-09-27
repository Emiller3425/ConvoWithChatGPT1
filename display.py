import pygame
from constants import BUTTON_COLOR, BUTTON_TEXT_COLOR, BUTTON_FONT_SIZE, SCREEN_COLOR

def draw_screen(screen, calculator):
    # Draw the calculator screen
    screen_rect = pygame.Rect(50, 50, 300, 100)
    pygame.draw.rect(screen, SCREEN_COLOR, screen_rect)
    screen_text = calculator.get_display_text()
    draw_text(screen, screen_text, screen_rect.center, (0, 0, 0))

def draw_button(screen, button):
    button.draw(screen)

def draw_text(screen, text, pos, color):
    font = pygame.font.Font(None, BUTTON_FONT_SIZE)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)