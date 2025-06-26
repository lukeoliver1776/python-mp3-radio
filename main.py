import random
import pygame
import time

from pathlib import Path

def play_radio():
    global radio_running
    radio_running = True

    music_folder = Path(__file__).parent / "music"

    pygame.mixer.init()

    while True:
        songs = list(music_folder.iterdir())
        random.shuffle(songs)

        for song in songs:
            pygame.mixer.music.load(str(song))
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if not radio_running:
                    pygame.mixer.music.stop()
                    return
            time.sleep(1)

radio_running = False

def stop_radio():
    global radio_running
    radio_running = False
    pygame.mixer.music.stop()