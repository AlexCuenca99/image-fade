import pygame
import time
import sys

FADE_IN_TIME = 20
FADE_OUT_TIME = 20
FADE_IN_EASING = lambda x: x
FADE_OUT_EASING = lambda x: x

pygame.init()
clock = pygame.time.Clock()
size = width, height = 800, 800

screen = pygame.display.set_mode(size)

img_1 = pygame.image.load("./src/image_1.png").convert_alpha()  # Ensure the image supports per-pixel alpha

image_position = img_1.get_rect(center=(width / 2, height / 2))

ST_FADEIN = 0
ST_FADEOUT= 1

state = ST_FADEIN
last_state_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    state_time = time.time() - last_state_time
    
    if state == ST_FADEIN:
        if state_time >= FADE_IN_TIME:
            state = ST_FADEOUT
            last_state_time = time.time()
    elif state == ST_FADEOUT:
        if state_time >= FADE_OUT_TIME:
            state = ST_FADEIN
            last_state_time = time.time()
    else:
        raise ValueError("Invalid state")

    if state == ST_FADEIN:
        alpha = FADE_IN_EASING(1.0 * state_time / FADE_IN_TIME)
    elif state == ST_FADEOUT:
        alpha = 1. - FADE_OUT_EASING(1.0 * state_time / FADE_OUT_TIME)
    else:
        raise ValueError("Invalid state")
    
    surf2 = pygame.Surface((image_position.width, image_position.height), pygame.SRCALPHA)  # Create a surface with per-pixel alpha
    surf2.fill((0, 0, 0, int(255 * (1 - alpha))))  # Fill it with black color and the desired alpha level
    
    screen.fill((0, 0, 0))
    screen.blit(img_1, (0,0))
    screen.blit(surf2, image_position)
    
    pygame.display.flip()
    clock.tick(60)
