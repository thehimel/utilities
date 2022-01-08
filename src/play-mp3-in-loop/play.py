import time
from pathlib import Path
import pygame


interval = 4.0
volume = 0.009
start_time = time.time()
audio = Path("audio.mp3").resolve()
print(audio)

while True:
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio)
    sound.set_volume(volume)  # 0.5 = 50% volume
    sound.play()
    time.sleep(interval)
