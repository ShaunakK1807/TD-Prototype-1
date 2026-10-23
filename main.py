import pygame as pg 
import numpy as np  
import constants as c  

# Initialise all available Pygame modules.
pg.init()

# Create a clock object so the game loop can run at a consistent frame rate.
clock = pg.time.Clock() 

# Create the game window using the dimensions stored in the constants module.
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pg.RESIZABLE)
# Set the text shown in the window title bar.
pg.display.set_caption("TD Prototype 1")

# Load the backdrop and scale it to the initial window size.
background_image = pg.image.load("Backgrounds/TD-background.png").convert()
background = pg.transform.scale(background_image, screen.get_size())

# ---------- Colour palette ----------
GOLD = (150, 105, 40)
GREY = (160, 160, 160)
BLACK = (0, 0, 0)


# Define the button's position and size.
button_rect = pg.Rect(540, 320, 200, 80)
# Store the button's grey colour as red, green, and blue values.
button_colour = GREY
# Load the local Cinzel font for the button label.
button_font = pg.font.Font("Fonts/Cinzel-Bold.ttf", 32)
# Render the button label as black text with no background box.
button_text = button_font.render("Click me", True, BLACK)
# Load the Cinzel Bold font at a larger size for the title.
title_font = pg.font.Font("Fonts/Cinzel-Bold.ttf", 64)
# Render the title text in white.
title_text = title_font.render("Tower defence", True, GOLD)



run = True
while run:
    #Event handling 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            # Video resize event to handle window resizing
        elif event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode(event.size, pg.RESIZABLE)
            background = pg.transform.scale(background_image, screen.get_size()) # Scale the background to the new window size
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Detect whether the click position is inside the button rectangle.
            if button_rect.collidepoint(event.pos):
                # Report the click without changing the button's appearance or state.
                print("Button clicked")

    
    screen.blit(background, (0, 0))  # Draw the background image at the top-left corner of the window.
    
    # Centre the title horizontally using the current window width, 20px from the top.
    title_rect = title_text.get_rect(midtop=(screen.get_width() // 2, 70))
    # Draw the title on the screen.
    screen.blit(title_text, title_rect)

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

