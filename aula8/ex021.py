import pygame

pygame.mixer.init()
pygame.mixer.music.load("vou-te-processar-amigao.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()
