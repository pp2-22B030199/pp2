import pygame
import os
import re

file = []
def name(n):
    font = pygame.font.SysFont("calibri", 60)
    song = font.render(file[n], True, (100, 100, 100))
    screen.blit(song, (100, 100))
    pygame.display.update()
with os.scandir() as entries:
    for entry in entries:
        if entry.is_file():
            if re.findall(".mp3", entry.name):
                file.append(entry.name)

print(file)

pygame.init()
pygame.mixer.init()
size = weight, height = (600, 600)
ORANGE = (255, 165, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music player")
screen.fill(ORANGE)

font = pygame.font.SysFont("Arial Black", 60)

text = font.render("Music player", True, (100, 100, 100))
SONG_END = pygame.USEREVENT + 1
pygame.mixer_music.set_endevent(SONG_END)
pygame.mixer_music.load(file[0])
pygame.mixer_music.play()
done = False
cnt = 0
pos = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cnt +=1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer_music.load(file[pos])
                pygame.mixer_music.play()
                cnt = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cnt -= 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer_music.load(file[pos])
                pygame.mixer_music.play()
                cnt = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pause = not pause
            if pause:
                pygame.mixer_music.pause()
                # pygame.mixer_music.play()
        if event.type == SONG_END:
            cnt += 1
            if cnt == 2:
                cnt = 0
            else:
                pos += cnt
                pygame.mixer_music.load(file[pos])
                pygame.mixer_music.play()
                cnt = 0
    name(pos)
    screen.fill(ORANGE)
    # screen.blit(text, (100, 100))

    screen.blit(text, (100, 250))
    pygame.display.update()

pygame.quit()