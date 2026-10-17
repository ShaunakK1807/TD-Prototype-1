import pygame as pg
import numpy as np
import constants as c
#initialise pygame
pg.init()


#create clock object to control the frame rate
clock = pg.time.Clock()


#create the game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
#set caption for the game window
pg.display.set_caption("TD Prototype 1")

font = pg.font.Font(None, 36)
button_font = pg.font.Font(None, 32)
test_button = pg.Rect(
    (c.SCREEN_WIDTH - 220) // 2,
    (c.SCREEN_HEIGHT - 60) // 2,
    220,
    60,
)
button_clicks = 0
button_message = "Click the button to test it"

run = True
while run:
    #event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if test_button.collidepoint(event.pos):
                button_clicks += 1
                button_message = f"Button clicked {button_clicks} time(s)"

    mouse_position = pg.mouse.get_pos()
    button_colour = (70, 150, 220) if test_button.collidepoint(mouse_position) else (45, 105, 170)

    screen.fill((25, 30, 45))
    title = font.render("Tower Defence Prototype", True, (240, 240, 240))
    message = font.render(button_message, True, (220, 220, 220))
    button_label = button_font.render("Test Button", True, (255, 255, 255))

    screen.blit(title, title.get_rect(center=(c.SCREEN_WIDTH // 2, 120)))
    screen.blit(message, message.get_rect(center=(c.SCREEN_WIDTH // 2, 220)))
    pg.draw.rect(screen, button_colour, test_button, border_radius=8)
    screen.blit(button_label, button_label.get_rect(center=test_button.center))
    pg.display.flip()
    clock.tick(c.FPS) #set the frame rate to 60 fps


pg.quit()
