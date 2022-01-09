"""
Issue: Bluetooth speaker turns off automatically.
Solution: Play an audio file with an interval.
The volume is almost 0.
The purpose is to send an audio signal to the speaker.
"""

import argparse
import time
from pathlib import Path
import pygame


if __name__ == "__main__":
    """Main function."""

    default_interval = 540.0
    default_volume = 0.0001

    parser = argparse.ArgumentParser(description="Play an audio file with an interval.")
    parser.add_argument(
        "path", metavar="path", type=str, help="Path to the audio file."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=float,
        default=default_interval,
        help="Playing interval.",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--volume",
        type=float,
        default=default_volume,
        help="Volume of the audio.",
        required=False,
    )
    args = parser.parse_args()

    file_path = Path(args.path)
    if not file_path.is_file():
        print(f"ERROR: File not found: {file_path}")
        exit(1)

    audio = file_path.resolve()
    interval = args.interval
    volume = args.volume

    while True:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(audio)
        sound.set_volume(volume)  # 0.5 = 50% volume
        sound.play()
        time.sleep(interval)
