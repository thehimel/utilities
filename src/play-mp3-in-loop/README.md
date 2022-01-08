# play-mp3-in-loop

Issue: Bluetooth speaker turns off automatically.
Solution: Play an audio file with an interval.

## Usage

* Create a directory in the OS and copy audio.mp3, play.bat, and play.py to the directory.
* Create a python virtual environment in that directory and install the requirements.
* Configure the file [play.bat](play.bat) with the python location.
  * Example: `C:\s\play\venv\Scripts\python C:\s\play\play.py`
* Add this file to the system startup.
  * Search for `run` and type `shell:startup`.
  * Paste a shortcut to the file here.
