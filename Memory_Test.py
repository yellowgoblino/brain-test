#import required libraries
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from wonderwords import RandomWord
import pygame
import random

def Memory_Test(window):

    pygame.init()

    #window setup
    window_width, window_height = 1280, 720
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Brain Benchmark')
    width = window.get_width()
    height = window.get_height()
    center = (window_height/2, window_width/2)

    #colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    txt_colour = (255, 255, 255)

    #random word generation
    seen_words = []
    
    #audio
    good_click_audio = pygame.mixer.Sound("ding.mp3")
    bad_click_audio = pygame.mixer.Sound("wrong_ding.mp3")
    endgame_sound = pygame.mixer.Sound("tada.mp3")

    #fonts
    font = pygame.font.Font(None, 36)
    announce_font = pygame.font.Font(None, 72)

    #misc
    score = seen_words.__len__()
    lives = 3
    fps = 60
    game_state = "start"

    #function makes seen words show up 33% of the time
    def update_shown_word(): 
        if random.random() > 0.33 or seen_words == []:
            ran_word = RandomWord()
            return ran_word.word(word_min_length=3, word_max_length=5)
        else:  
            return random.choice(seen_words)

    current_word = update_shown_word()

    class User_interface():
        
        def main_screen(self):
            window.fill(black)
            lives_txt = announce_font.render(f"Lives: {lives}", True, txt_colour)
            window.blit(lives_txt, (window_width - 225, 10))

        def saw_new_buttons(self):
            self.button_new = pygame.draw.rect(window, green, ((320, 400), (300, 100)))
            self.button_seen = pygame.draw.rect(window, red, ((window_width-640, 400), (300, 100)))
            button_new_txt = announce_font.render("NEW", True, txt_colour)
            button_seen_txt = announce_font.render("SEEN", True, txt_colour)
            button_new_txt_rect = button_new_txt.get_rect(center=(470, 450))
            button_seen_txt_rect = button_seen_txt.get_rect(center=(790, 450))
            window.blit(button_new_txt, button_new_txt_rect)
            window.blit(button_seen_txt, button_seen_txt_rect)
            score_txt = announce_font.render(f"Score: {score}", True, txt_colour)
            score_rect = score_txt.get_rect(center=(window_width / 2, window_height /2-150))
            window.blit(score_txt, score_rect)
        
        def display_word(self):
            display_word_txt = announce_font.render(current_word, True, (txt_colour))
            display_word_rect = display_word_txt.get_rect(center=(window_width / 2, window_height /2 -50))
            window.blit(display_word_txt, display_word_rect)

    user_interface = User_interface()

    #clickable area
    button_new_rect = pygame.Rect(320, 400, 300, 100)
    button_seen_rect = pygame.Rect(window_width-640, 400, 300, 100)

    running = True

    while running:
        #main logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "start":
                    game_state = "waiting_click"
                elif game_state == "waiting_click":
                    mouse_pos = pygame.mouse.get_pos()
                    if button_new_rect.collidepoint(mouse_pos):
                        if current_word in seen_words:
                            pygame.mixer.Sound.play(bad_click_audio)
                            lives -= 1
                        else:
                            pygame.mixer.Sound.play(good_click_audio)
                            score += 1
                            seen_words.append(current_word)
                        current_word = update_shown_word()
                    elif button_seen_rect.collidepoint(mouse_pos):
                        if current_word in seen_words:
                            pygame.mixer.Sound.play(good_click_audio)
                            score += 1
                        else:
                            pygame.mixer.Sound.play(bad_click_audio)
                            lives -= 1
                            seen_words.append(current_word)
                        current_word = update_shown_word()
                    if lives <= 0:
                        game_state = "end"
        #visual updates                    
        if game_state == "start":
            user_interface.main_screen()
            intro_txt = font.render("Memory test: If you haven't seen the displayed word before", True, (txt_colour))
            display_word_rect = intro_txt.get_rect(center=(window_width / 2, window_height /2 -50))
            window.blit(intro_txt, display_word_rect)
            intro2_txt = font.render("click NEW, if you have, click seen. You have 3 lives.", True, (txt_colour))
            display_word_rect = intro_txt.get_rect(center=(window_width / 2, window_height /2))
            window.blit(intro2_txt, display_word_rect)
            intro3_txt = font.render("Click to continue.", True, (txt_colour))
            display_word_rect = intro_txt.get_rect(center=(window_width / 2, window_height /2 + 50))
            window.blit(intro3_txt, display_word_rect)
        
        if game_state == "waiting_click":
            user_interface.main_screen()
            user_interface.saw_new_buttons()
            user_interface.display_word()
        
        if game_state == "end":
            window.fill(black)
            pygame.mixer.Sound.play(endgame_sound)
            end_txt = announce_font.render(f"Score: {score}", True, (txt_colour))
            display_word_rect = end_txt.get_rect(center=(window_width / 2, window_height /2))
            window.blit(end_txt, display_word_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        pygame.display.update()
    return "main menu"