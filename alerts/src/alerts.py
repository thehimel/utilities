"""
Plays alerts for given tasks.
"""

from pathlib import Path
from datetime import datetime
import pytz
from gtts import gTTS
from audioplayer import AudioPlayer
from apscheduler.schedulers.blocking import BlockingScheduler


def audio(text: str, title: str) -> AudioPlayer:
    """Convert text to audio."""
    title = f"{title}.mp3" if not title.endswith(".mp3") else title
    audio_path = Path("audio")
    audio_path.mkdir(parents=True, exist_ok=True)  # Create directory if doesn't exists.
    audio_path = Path(audio_path / title).as_posix()
    speech = gTTS(text=text, lang='en', slow=False)  # Due to slow=False, the converted audio should have a high speed.
    speech.save(audio_path)
    return AudioPlayer(audio_path)


def drink_water() -> None:
    """Play audio to drink water."""
    audio_drink_water.play(block=False)


def eat_fruits() -> None:
    """Play audio to eat fruits."""
    audio_eat_fruits.play(block=False)


if __name__ == "__main__":
    TONE = "Ten tena!" * 3
    audio_drink_water = audio(text=f"{TONE} Please drink water!", title="drink_water")
    audio_eat_fruits = audio(text=f"{TONE} Please eat fruits!", title="eat_fruits")

    try:
        scheduler = BlockingScheduler(timezone=pytz.timezone("Europe/Berlin"))
        scheduler.add_job(eat_fruits, "cron", hour=16, minute=0)  # Run this job everyday at 16:00 PM.
        scheduler.add_job(drink_water, "interval", seconds=3600, next_run_time=datetime.now())
        scheduler.start()
    except KeyboardInterrupt:
        print("Stay healthy!")
