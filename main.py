#Summer Checkers
import pygame
import sys
from button import Button
from pyvidplayer import Video
from summer_checkers.constants import BLACK, WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from summer_checkers.game import Game

FPS = 60
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SummerCheckers')

new_icon = pygame.image.load("assets/new_icon.jpg")
pygame.display.set_icon(new_icon)

BG = pygame.image.load("assets/Beach.jpg")

BGM = pygame.mixer.music.load("sound/background_music.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

vid = Video ("Summer Checkers Video.mp4")
vid.set_size((800, 800))

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color, y_offset=0, size="small"):
    if size == "small":
        font_size = 40
    elif size == "medium":
        font_size = 50
    elif size == "large":
        font_size = 80
    else:
        raise ValueError("Invalid size specified")

    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(msg, True, color)
    text_rect = screen_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    WIN.blit(screen_text, text_rect)

def pause():
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        WIN.blit(BG, (0, 0))
        message_to_screen("GAME IS PAUSED", BLACK, -100, size="large")
        message_to_screen("Press C to continue or Q to quit.", BLACK, 25)
        pygame.display.update()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def intro():
    while True:
        vid.draw(WIN, (0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_menu()
                
def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        game = Game(WIN)  # Create a new game instance
        
        while True:  # Game loop
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:  
                        break  
                    
            game.update()

            WIN.blit(BG, (0, 0))

            winner = game.winner()
            if winner is not None:
                show_winner_screen(winner)
                break 

    pygame.quit()

def show_winner_screen(winner):
    screen_text = "2nd player wins! press q to quit and press r to retry" if winner == WHITE else "1st player wins! press q to quit and press r to retry"
    message_to_screen(screen_text, BLACK, size="small")
    pygame.display.update()
    pygame.time.delay(6000) 

def main_menu():
    pygame.display.set_caption('Summer Checkers')
    
    while True:
        WIN.blit(BG, (0, 0))
    
        MOUSE = pygame.mouse.get_pos()
        
        START_BUTTON = Button(390, 400, "assets/START_BUTTON.png", "assets/START_BUTTON_Hover.png")
        EXIT_BUTTON = Button(390, 600, "assets/EXIT_BUTTON.png", "assets/EXIT_BUTTON_hover.png")
        
        for button in [START_BUTTON, EXIT_BUTTON]:
            button.hover_button(MOUSE)
            button.update(WIN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MOUSE):
                    main()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if EXIT_BUTTON.checkForInput(MOUSE):
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

intro()
