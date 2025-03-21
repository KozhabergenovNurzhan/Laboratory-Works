import pygame
import os
from mutagen.mp3 import MP3

pygame.init()
pygame.mixer.init()

background = pygame.image.load("images/boombox.png")
WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

MUSIC_FOLDER = "music"
songs = [song for song in os.listdir(MUSIC_FOLDER) if song.endswith(".mp3")]

if not songs:
    print("No music files found!")
    exit()

current_index = 0
paused = False

def get_song_length(song_path):
    return MP3(song_path).info.length  

pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
pygame.mixer.music.play()
song_length = get_song_length(os.path.join(MUSIC_FOLDER, songs[current_index]))

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.play()

def stop_music():
    global paused
    pygame.mixer.music.stop()
    paused = True

def next_track():
    global current_index, paused, song_length
    current_index = (current_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
    pygame.mixer.music.play()
    song_length = get_song_length(os.path.join(MUSIC_FOLDER, songs[current_index]))
    paused = False

def previous_track():
    global current_index, paused, song_length
    current_index = (current_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
    pygame.mixer.music.play()
    song_length = get_song_length(os.path.join(MUSIC_FOLDER, songs[current_index]))
    paused = False

run = True
while run:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    elapsed_time = pygame.mixer.music.get_pos() / 1000  
    progress = min(elapsed_time / song_length, 1)  

    pygame.draw.rect(screen, BLACK, (50, HEIGHT + 5, WIDTH - 100, 10))  
    pygame.draw.rect(screen, BLUE, (50, HEIGHT + 5, (WIDTH - 100) * progress, 10))  

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
            elif event.key == pygame.K_q:
                stop_music()
                run = False

pygame.quit()
