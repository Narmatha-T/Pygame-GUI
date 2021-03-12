import math
import pygame
from os import system
from pygame import mixer
from random import randint

def animation():
    # Intialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((1494, 600))

    # Background
    background1 = pygame.image.load('bg1.jpg')
    background2 = pygame.image.load('bg2.jpg')

    # Sound
    mixer.music.load("RUDE - Eternal Youth.mp3")
    mixer.music.play(-1)  

    # Caption and Icon
    pygame.display.set_caption("VISUAL TEXT ADVENTURE")
    icon = pygame.image.load('location.png')
    pygame.display.set_icon(icon)

    # button fonts
    start_font = pygame.font.Font('freesansbold.ttf', 34)
    instructions_font = pygame.font.Font('freesansbold.ttf', 34)
    quit_font = pygame.font.Font('freesansbold.ttf', 34)
    game_name_font = pygame.font.Font('freesansbold.ttf', 64)
    screen_name_font = pygame.font.Font('freesansbold.ttf', 40)

    def start_text():
        start_text = start_font.render("START", True, (0, 0, 0))
        screen.blit(start_text, (465, 380))

    def instructions_text():
        instructions_text = instructions_font.render("INSTRUCTIONS", True, (0, 0, 0))
        screen.blit(instructions_text, (630, 380))

    def quit_text():
        quit_text = quit_font.render("EXIT", True, (0, 0, 0))
        screen.blit(quit_text, (955, 380))

    def game_name():
        screen_name_text = game_name_font.render("VISUAL ADVENTURE", True, (141, 182, 205))
        screen.blit(screen_name_text, (425, 300))

    def player_name():
        screen_name_text = screen_name_font.render("ENTER THE PLAYER NAME:", True, (245, 20, 222))
        screen.blit(screen_name_text, (480, 270))


    def game_menu():
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(630, 350, 140, 32)
        color_inactive = pygame.Color('#3333FF')
        color_active = pygame.Color('#F514DE')
        color = color_inactive
        active = False
        text = ''
        done = False
        response = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        while True:
            # RGB = Red, Green, Blue
            screen.fill((0, 0, 0))

            # Background Image
            screen.blit(background2, (0, -130))

            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            player_name()
            pygame.display.update()

    def instructions():
        print("Enter numbers for your choices")
        print("Think wise!!")

    def start_menu():
        while True:
            # RGB = Red, Green, Blue
            screen.fill((0, 0, 0))

            # Background Image
            screen.blit(background1, (0, 0))

            # game name
            game_name()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                button1 = pygame.Rect(445, 370, 150, 50)
                button_clr1 = pygame.Rect(447, 372, 145, 45)
                pygame.draw.rect(screen, (0, 0, 0), button1, 5)
                pygame.draw.rect(screen, (0, 76, 153), button_clr1, 0)
                start_text()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button1.collidepoint(event.pos):
                            pygame.quit()
                            final_game()  # calling the text adv

                # button2
                button2 = pygame.Rect(610, 370, 310, 50)
                button_clr2 = pygame.Rect(612, 372, 306, 46)
                pygame.draw.rect(screen, (0, 0, 0), button2, 5)
                pygame.draw.rect(screen, (0, 76, 153), button_clr2, 0)
                instructions_text()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button2.collidepoint(event.pos):
                            pygame.quit()
                            instructions()
                            quit()

                # button3
                button3 = pygame.Rect(935, 370, 120, 50)
                button_clr3 = pygame.Rect(937, 372, 116, 46)
                pygame.draw.rect(screen, (0, 0, 0), button3, 5)
                pygame.draw.rect(screen, (0, 76, 153), button_clr3, 0)
                quit_text()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button3.collidepoint(event.pos):
                            pygame.quit()
                            print("Thanks")
                            quit()
                pygame.display.update()

    start_menu()

def main():
    animation()
main()