from tkinter import *
import threading
from main import play_radio, stop_radio
import pygame

window = Tk()
window.geometry("420x300")
window.title("Real Country Radio")
window.resizable(False, False)

title_label = Label(window, text="Real Country Radio", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

song_label = Label(window, text="No song playing", font=("Helvetica", 14), fg="gray")
song_label.pack(pady=20)

def start_playback():
    song_label.config(text="Starting playback...")
    threading.Thread(target=play_radio, daemon=True).start()

def stop_playback():
    song_label.config(text="Playback stopped")
    stop_radio()

def update_volume(val):
    volume = float(val) / 100
    if pygame.mixer.get_init():
        pygame.mixer.music.set_volume(volume)

start_button = Button(window, text="Start", font=("Helvetica", 12), width=12, command=start_playback)
start_button.pack(pady=10)

stop_button = Button(window, text="Stop", font=("Helvetica", 12), width=12, command=stop_playback)
stop_button.pack(pady=5)

volume_slider = Scale(window, from_=0, to=100, orient=HORIZONTAL, label="Volume", command=update_volume)
volume_slider.set(50)
volume_slider.pack(pady=15)

window.mainloop()
