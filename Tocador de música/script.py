import pygame  

#iniciar pygame
pygame.init()

#carregar música
pygame.mixer.music.load('audio.mp3')

#tocar música
pygame.mixer.music.play()

#esperar música acabar para parar de tocar
pygame.mixer.music.wait()
