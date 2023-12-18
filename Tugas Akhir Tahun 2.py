# Membuat prorgram sederhana 
# tasbih digital menggunakan Python3

import pygame
from pygame.locals import *

# Warna (R, G, B)
hitam = (0, 0, 0)
putih = (255, 255, 255)
gray = (200, 200, 200)
merah = (255, 0, 0)

# set ukuran layar
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Tasbih Digital Python') 
background = 'gray'

# variable tasbih
count = 0

# Looping
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            count += 1
    
    #identifikasi font
    font_judul = pygame.font.SysFont('arial', 40)
    font_teks = pygame.font.SysFont('arial', 50)
    font_angka = pygame.font.SysFont('arial', 150)

    judul = font_judul.render('Tasbih Digital Python', True, hitam)
    teks = font_teks.render('Count:', True, hitam)
    angka = font_angka.render(f'{count}', True, hitam)

    #tampilkan teks di layar
    screen.fill(background)
    screen.blit(judul, (180, 10))
    screen.blit(teks, (280, 30))
    screen.blit(angka, (280, 80))
    pygame.display.update()

pygame.quit()


