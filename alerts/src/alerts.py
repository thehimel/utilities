"""
Plays alerts for given tasks.
"""

import json
import logging
from pathlib import Path
import pytz
from gtts import gTTS
from audioplayer import AudioPlayer
from apscheduler.schedulers.blocking import BlockingScheduler


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(levelname)s : %(message)s')
FILE_PATH = Path(__file__).parent.resolve()  # Path for the directory of this file.


def audio(text: str, title: str) -> AudioPlayer:
    """Convert text to audio."""
    title = f"{title}.mp3" if not title.endswith(".mp3") else title
    audio_path = Path(FILE_PATH / "audio")
    audio_path.mkdir(parents=True, exist_ok=True)  # Create directory if doesn't exists.
    audio_path = Path(audio_path / title).as_posix()
    speech = gTTS(text=text, lang="en", slow=False)  # Due to slow=False, the converted audio should have a high speed.
    speech.save(audio_path)
    return AudioPlayer(audio_path)


def play(audio_player: AudioPlayer, schedule: dict) -> None:
    """Play the audio"""
    logging.info(f"Playing: {schedule}")
    audio_player.play(block=False)


def handle() -> None:
    """Handler for the execution of jobs."""
    scheduler = BlockingScheduler(timezone=pytz.timezone("Europe/Berlin"))
    schedule_types = {"interval": "interval", "cron": "cron"}
    tone = "Ten tena! " * 3
    audio_files = {}

    with open(Path(FILE_PATH / "schedules.json"), encoding="utf-8") as schedules_json:
        schedules = json.load(schedules_json)

    for schedule in schedules:
        if schedule["type"].lower() == schedule_types["interval"]:
            title = schedule["title"]
            if title not in audio_files:
                audio_files[title] = audio(text=f"{tone}{schedule['message']}", title=title)
            scheduler.add_job(
                play,  # function name
                schedule_types["interval"],
                [audio_files[title], schedule],  # function parameters
                seconds=schedule["interval"],
            )
        elif schedule["type"].lower() == schedule_types["cron"]:
            title = schedule["title"]
            if title not in audio_files:
                audio_files[title] = audio(text=f"{tone}{schedule['message']}", title=title)
            # Run this job everyday at a specific time.
            scheduler.add_job(
                play,
                schedule_types["cron"],
                [audio_files[title], schedule],
                hour=schedule["time"]["hour"],
                minute=schedule["time"]["minute"]
            )
        else:
            logging.error(f"Invalid schedule type: {schedule['type']} for schedule: {schedule}")
    scheduler.start()


if __name__ == "__main__":
    try:
        handle()
    except KeyboardInterrupt:
        logging.info("Stay healthy!")
