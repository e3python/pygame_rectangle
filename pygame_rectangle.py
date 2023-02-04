import sys
import pygame


def pygame_rectangle():
    # Initialize pygame
    pygame.init()

    # Set up the drawing window 150x150 pixels
    window_size = (150, 150)
    surface = pygame.display.set_mode(window_size)

    # Set the title (caption) of the window
    title = "pygame rectangle"
    pygame.display.set_caption(title)

    # Create a rect
    point = (50, 50)    # top left corner of rectangle
    size = (30, 30)     # width and height of rectangle
    fill_color = "lightblue"
    border_color = "black"
    border_width = 3
    rectangle = pygame.Rect(point, size)

    # event loop for program
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        # Fill the background of the surface with white
        background_color = "lightgray"
        surface.fill(background_color)

        # Draw the rectangle in light blue on the surface
        pygame.draw.rect(surface, fill_color, rectangle)

        # Draw a black outline on the rectangle by specifying a border width of 3
        pygame.draw.rect(surface, border_color, rectangle, border_width)


        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    pygame_rectangle()
    