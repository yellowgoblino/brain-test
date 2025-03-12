from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import random

def Reaction_Time_Test(window):

    pygame.init()

    #window setup
    window_width, window_height = 1280, 720
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Brain Benchmark')

    #colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    txt_colour = (255, 255, 255)

    #framerate
    fps = 60

    #audio
    good_click_audio = pygame.mixer.Sound("ding.mp3")
    endgame_sound = pygame.mixer.Sound("tada.mp3")

    #time settings
    clock = pygame.time.Clock()
    remaining_checks = 5
    ready_time = random.randint(500, 3000)

    #fonts
    font = pygame.font.Font(None, 36)
    announce_font = pygame.font.Font(None, 72)

    #misc
    game_state = "start"
    trials = 0
    total_time = 0

    running = True
    while running:
        #getting a way to track time
        clock.tick(fps)
        time = pygame.time.get_ticks()
        #main logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "start":
                    game_state = "wait"
                    window.fill(red)
                    ready_txt = announce_font.render("Get ready!", True, txt_colour)
                    ready_rect = ready_txt.get_rect(center=(window_width / 2, window_height / 2))
                    window.blit(ready_txt, ready_rect)
                    start_time = time + ready_time
                if game_state == "waiting_click":
                    game_state = "wait"
                    reaction_time = time - start_time
                    start_time = time + ready_time
                    trials += 1
                    total_time = total_time + reaction_time
                    window.fill(red)
                    pygame.mixer.Sound.play(good_click_audio)
                    reaction_txt = announce_font.render(f"{reaction_time}ms", True, txt_colour)
                    reaction_rect = reaction_txt.get_rect(center=(window_width / 2, window_height / 2))
                    window.blit(reaction_txt, reaction_rect)
        #end condition
        if game_state == "wait":
            if trials <= 5 and time >= start_time:
                game_state = "waiting_click"
            if trials > 5:
                game_state = "end"
        #visual updates
        if game_state == "start":
            window.fill(red)
            start_txt = announce_font.render("Press anything to start", True, txt_colour)
            start_rect = start_txt.get_rect(center=(window_width / 2, window_height / 2))
            window.blit(start_txt, start_rect)
        if game_state == "waiting_click":
            window.fill(green)
            wait_txt = announce_font.render("CLICK", True, txt_colour)
            wait_rect = wait_txt.get_rect(center=(window_width / 2, window_height / 2))
            window.blit(wait_txt, wait_rect)
        if game_state == "end":
            window.fill(black)
            pygame.mixer.Sound.play(endgame_sound)
            average_reaction = total_time/5
            end_txt = announce_font.render(f"Your average reaction time was {average_reaction}ms!", True, txt_colour)
            end_rect = end_txt.get_rect(center=(window_width / 2, window_height / 2))
            window.blit(end_txt, end_rect)
            pygame.display.update()
            pygame.time.delay(3000)
            running = False   
        pygame.display.update()
    return "main menu"
    


        


