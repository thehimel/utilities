"""
Plays alerts for given tasks.
"""

import time
from gtts import gTTS
from pathlib import Path
from audioplayer import AudioPlayer


if __name__ == "__main__":
    """Main function."""

    text = 'Ten tena! Ten tena! Ten tena! Please drink water!'
    language = 'en'
    # Due to slow=False , the converted audio should  have a high speed
    speech_drink_water = gTTS(text=text, lang=language, slow=False)
    path_drink_water = Path("speech_drink_water.mp3").as_posix()
    speech_drink_water.save(path_drink_water)
    interval_drink_water = 10
    player_drink_water = AudioPlayer(path_drink_water)

    while True:
        player_drink_water.play(block=False)
        time.sleep(interval_drink_water)
