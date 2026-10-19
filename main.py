import pygame as pg 
import numpy as np  
import constants as c  

# Initialise all available Pygame modules.
pg.init()

# Create a clock object so the game loop can run at a consistent frame rate.
clock = pg.time.Clock()

# Create the game window using the dimensions stored in the constants module.
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
# Set the text shown in the window title bar.
pg.display.set_caption("TD Prototype 1")

# Define the button's position and size.
button_rect = pg.Rect(540, 320, 200, 80)
# Store the button's grey colour as red, green, and blue values.
button_colour = (160, 160, 160)
# Load a Helvetica font for the button label.
main_font = pg.font.SysFont("Helvetica", 32)
# Render the button label as black text with no background box.
button_text = main_font.render("Click me", True, (0, 0, 0))


run = True
while run:
    #Event handling 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Detect whether the click position is inside the button rectangle.
            if button_rect.collidepoint(event.pos):
                # Report the click without changing the button's appearance or state.
                print("Button clicked")

    
    background_colour = (255, 255, 255) # White
    screen.fill(background_colour)

    # Draw the grey button on the screen.
    pg.draw.rect(screen, button_colour, button_rect)
    # Position the text in the centre of the button.
    text_position = button_text.get_rect(center=button_rect.center)
    # Draw the button text at the calculated position.
    screen.blit(button_text, text_position)

    # Show the completed frame in the game window.
    pg.display.flip()
    clock.tick(c.FPS)

# Shut down Pygame cleanly after the game loop ends.
pg.quit()
