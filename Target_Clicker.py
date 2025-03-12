#import required libraries
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import random
import math

def Target_Clicker(window):

    pygame.init()

    #window setup
    window_width, window_height = 1280, 720
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Brain Benchmark')

    #colours
    white = (255, 255, 255)

    #audio
    target_hit_sound = pygame.mixer.Sound("target_hit.mp3")
    endgame_sound = pygame.mixer.Sound("tada.mp3")


    #timer
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    running = True
    game_duration = 30

    #difficulty variables
    game_duration = 30
    circle_radius = 25
    score = 0  

    #fonts
    font = pygame.font.Font(None, 36)
    announce_font = pygame.font.Font(None, 72)

    class Target(object):
        def __init__(self):
            self.target_spawn()
        
        def target_spawn(self):
            #less than screen resolution so targets arent by the edge of the screen
            self.spawn_x = random.randint(128, 1152)
            self.spawn_y = random.randint(144, 576)
        
        def target_drawing(self):
            pygame.draw.circle(window, white, (self.spawn_x, self.spawn_y), circle_radius)


    target = Target()

    #warmup screen
    ready_txt = announce_font.render("Get ready!", True, white)
    ready_rect = ready_txt.get_rect(center=(window_width / 2, window_height / 2))
    window.blit(ready_txt, ready_rect)
    pygame.display.update()
    pygame.time.delay(3000)

    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        target.target_drawing()
        #main logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                distance = math.hypot(mouse_pos[0] - target.spawn_x, mouse_pos[1] - target.spawn_y)
                if distance <= circle_radius:
                    score += 1
                    pygame.mixer.Sound.play(target_hit_sound)
                    target.target_spawn()
        
        #score and time remaining UI
        elapsed_time = (pygame.time.get_ticks() - start_ticks-3000) / 1000
        remaining_time = max(game_duration - elapsed_time, 0)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  
        timer_text = font.render(f"Time Left: {int(remaining_time)}s", True, (255, 255, 255))
        window.blit(score_text, (window_width - 175, 10))
        window.blit(timer_text, (window_width - 175, 30))
        

        pygame.display.update()
        
        if remaining_time <= 0:
            running = False

    #end screen
    window.fill((0, 0, 0))
    pygame.mixer.Sound.play(endgame_sound)
    endgame_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    endgame_rect = endgame_text.get_rect(center=(window_width/2, window_height/2 - 30))

    window.blit(endgame_text, endgame_rect)

    pygame.display.update()

    pygame.time.delay(3000)

    return "main menu"


