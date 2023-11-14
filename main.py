import pygame
import os
import random


pygame.init()

# Constant Variables
WIDTH = 1000
HEIGHT = 700
TITLE = "Team Vector"
VEL = 5
CLOCK = pygame.time.Clock()
FPS = 60



# Importing Images
ICON = pygame.image.load(os.path.join("Assets", "icon.png"))
Normal_BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Normal_Level_BG.png")), (WIDTH,HEIGHT))
Final_BG = pygame.image.load(os.path.join("Assets", "Final_Level_BG.png"))

HERO = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Robert.png")), (WIDTH/5, HEIGHT/3))
BOTS = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bots.png")), (142.85, 100))


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)



# Helping Functions
def draw_surface(hero_x, hero_y):
    WIN.blit(Normal_BG, (0,0))
    WIN.blit(HERO, (hero_x,hero_y))
    pygame.display.update()

def draw_bots(bot_num, bot_x, bot_y):
    WIN.blit(BOTS, (bot_x, bot_y))
    pygame.display.update()


def main():
    # Game Variables

    hero_x = 50     # MIN 10 , MAX 120
    hero_y = 375    # MIN 300, MAX 450 

    CLOCK.tick(FPS)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                pass

        key = pygame.key.get_pressed()
        # Robert Movement
        if key[pygame.K_w]:
            if hero_y > 300:
                hero_y -= VEL
        if key[pygame.K_a]:
            if hero_x > 3:
              hero_x -= VEL
        if key[pygame.K_s]:
            if hero_y < 450:
                hero_y += VEL
        if key[pygame.K_d]:
            if hero_x < 150:
                hero_x += VEL

    
        draw_surface(hero_x, hero_y)


if __name__ == "__main__":
    main()

