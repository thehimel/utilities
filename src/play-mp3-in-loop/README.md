# play-mp3-in-loop

Issue: Bluetooth speaker turns off automatically.
Solution: Play an audio file with an interval.

## Usage

```shell
$ python play.py -h

usage: play.py [-h] [-i INTERVAL] [-v VOLUME] path

Play an audio file with an interval.

positional arguments:
  path                  Path to the audio file.

options:
  -h, --help            show this help message and exit
  -i INTERVAL, --interval INTERVAL
                        Playing interval.
  -v VOLUME, --volume VOLUME
                        Volume of the audio.
```

### Examples

```shell
# Play audio.mp3 with the default interval and volume.
python play.py audio.mp3

# Play audio.mp3 with the default interval and 50% volume.
python play.py audio.mp3 -v 0.5

# Play audio.mp3 with an interval of 4 seconds and 90% volume.
python play.py audio.mp3 -i 4 -v 0.9
```

## How to Configure

* Create a directory in the OS and copy audio.mp3, play.bat, and play.py to the directory.
* Create a python virtual environment in that directory and install the requirements.
* Configure the file [play.bat](play.bat) with the python location.
  * Example: `C:\s\play\venv\Scripts\python C:\s\play\play.py C:\s\play\audio.mp3`
* Add this file to the system startup.
  * Search for `run` and type `shell:startup`.
  * Paste a shortcut to the file here.
