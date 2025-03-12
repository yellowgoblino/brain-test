#import required libraries
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sys
import random
from wonderwords import RandomWord
from Memory_Test import Memory_Test
from Reaction_Time_Test import Reaction_Time_Test
from Target_Clicker import Target_Clicker

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
white = (255, 255, 255)

#fonts
font = pygame.font.Font(None, 36)
announce_font = pygame.font.Font(None, 72)
title_font = pygame.font.Font(None, 120)

game_state = "main_menu"

class User_interface():
    def main_screen(self):
        window.fill(black)
        title_txt =  title_font.render("Brain Benchmark", True, white)
        title_txt_rect = title_txt.get_rect(center=(window_width/2, window_height/2-160))
        window.blit(title_txt, title_txt_rect)
    
    def button_TC(self):
        self.button_tc = pygame.draw.rect(window, white, ((320, 300), (300, 100)))
        self.button_tc_txt = announce_font.render("PRECISION", True, black)
        self.button_tc_txt_rect = self.button_tc_txt.get_rect(center=(470, 350))
        window.blit(self.button_tc_txt, self.button_tc_txt_rect)

    def button_RTT(self):
        self.button_rtt = pygame.draw.rect(window, white, ((320, 425), (300, 100)))
        self.button_rtt_txt = announce_font.render("REACTION", True, black)
        self.button_rtt_txt_rect = self.button_rtt_txt.get_rect(center=(470, 475))
        window.blit(self.button_rtt_txt, self.button_rtt_txt_rect)

    def button_MT(self):
        self.button_mt = pygame.draw.rect(window, white, ((window_width-640, 300), (300, 100)))
        self.button_mt_txt = announce_font.render("MEMORY", True, black)
        self.button_mt_txt_rect = self.button_mt_txt.get_rect(center=(790, 350))
        window.blit(self.button_mt_txt, self.button_mt_txt_rect)   

user_interface = User_interface()

#clickable area
button_TC_rect = pygame.Rect(320, 300, 300, 100)
button_RTT_rect = pygame.Rect(320, 425, 300, 100)
button_MT_rect = pygame.Rect(window_width-640, 300, 300, 100)

running = True

while running:
    #init UI
    user_interface.main_screen()
    user_interface.button_RTT()
    user_interface.button_TC()
    user_interface.button_MT()
    #main logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_TC_rect.collidepoint(mouse_pos):
                game_state = "Target_Clicker"
            if button_RTT_rect.collidepoint(mouse_pos):
                game_state = "Reaction_Time_Test"
            if button_MT_rect.collidepoint(mouse_pos):
                game_state = "Memory_Test"
        
    if game_state == "main menu":
        User_interface()
    if game_state == "Memory_Test":
        Memory_Test(window)
        game_state = "main menu"
    if game_state == "Reaction_Time_Test":
        Reaction_Time_Test(window)
        game_state = "main menu"
    if game_state == "Target_Clicker":
        Target_Clicker(window)
        game_state = "main menu"
        

    pygame.display.update()
#close with no crashes
pygame.display.quit()
sys.exit()
exit()