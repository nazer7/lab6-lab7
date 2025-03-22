import pygame
import keyboard
import os
import time
pygame.mixer.init()
playlist = [r"C:\Users\lenovo\Documents\ксм\BTS_-_House_of_Cards_56088027.wav"]
current_track = 0
def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    print(f"Playing: {os.path.basename(playlist[current_track])}")
def stop_music():
    pygame.mixer.music.stop()
    print("Stopped.")
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()
print("Music Player Controls: P = Play, S = Stop, N = Next, B = Previous, Q = Quit")
while True:
    if keyboard.is_pressed('p'):
        play_music()
        time.sleep(0.3)
    elif keyboard.is_pressed('s'):
        stop_music()
        time.sleep(0.3)
    elif keyboard.is_pressed('n'):
        next_track()
        time.sleep(0.3)
    elif keyboard.is_pressed('b'):
        previous_track()
        time.sleep(0.3)
    elif keyboard.is_pressed('q'):
        print("Exiting music player.")
        break
pygame.mixer.quit()





