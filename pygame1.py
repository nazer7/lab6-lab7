import pygame
import time
import math
pygame.init()
WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock_face = pygame.image.load("mickeyclock.jpeg").convert()
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
minute_hand = pygame.image.load("mickey_right_hand.png").convert_alpha()
second_hand = pygame.image.load("mickey_left_hand.png").convert_alpha()
minute_hand = pygame.transform.scale(minute_hand, (100, 20))  
second_hand = pygame.transform.scale(second_hand, (120, 15)) 
minute_rect = minute_hand.get_rect(center=CENTER)
second_rect = second_hand.get_rect(center=CENTER)
running = True
while running:
    screen.fill(WHITE)
    screen.blit(clock_face, (0, 0))
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    minute_angle = -(minutes * 6) 
    second_angle = -(seconds * 6)  
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    min_rect = rotated_minute.get_rect(center=CENTER)
    sec_rect = rotated_second.get_rect(center=CENTER)
    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft) 
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(1000)

pygame.quit()





