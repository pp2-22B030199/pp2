import pygame
import re
import datetime

pygame.init()

size = w,h = (1300,920)

time = datetime.datetime.now()
angle = -(int(time.strftime("%S"))) * 6 -6
angleM = -(int(time.strftime("%M"))) * 6 + (int(time.strftime("%S")) * 6 / 60) - 54

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center = rect.center )
    return new_image, rect

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Micky clock')

mickey = pygame.image.load('mickey2.jpg')
# minutes = pygame.image.load('2023-03-14 20.31.00.jpg')
seconds = pygame.image.load('2023-03-14 20.30.52.jpg')
minutes = pygame.image.load('2023-03-14 20.31.00.jpg')

imagem = pygame.Surface((w,h), pygame.SRCALPHA)
imagem.blit(minutes, (0, 0))
newm = imagem
rectm = imagem.get_rect(center = (w//2, h//2))

image = pygame.Surface((w,h), pygame.SRCALPHA)
image.blit(seconds, (0, 0))
new = image
rect = image.get_rect(center = (w//2, h//2))

clock = pygame.time.Clock()
done = False

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(mickey, (0, 0))
    screen.blit(imagem, rectm)
    screen.blit(image, rect)
    image, rect = rotate(seconds, rect, angle)
    imagem, rectm = rotate(minutes, rectm, angleM)

    angle -= 0.099
    angleM -= 0.099/60

    pygame.display.update()
pygame.quit()