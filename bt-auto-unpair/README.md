# Auto-Unpair DJI Mic 2 on macOS

Automatically unpair DJI Mic 2 from Mac when it disconnects.

## Install Required Tools

```bash
brew install blueutil
```

## Make the Script Executable

```bash
chmod +x ./unpair_dji_mic.sh
```

> Use `blueutil --paired` to find the Mac address for the first time.

## How to Use

* Run the script in the background.
* It will check the connection status with an interval of 5 seconds.
* If the DJI Mic 2 is paired and disconnected, it will automatically unpair it.
* To pair it again, you need to do it manually from the Bluetooth settings.
* On the transmitter, press and hold the power button for 3 seconds to turn it on and then press and hold the Link button for 3 seconds to enter pairing mode.
* To disconnect, simple turn off the transmitter.
* Within 5 seconds of disconnecting, the script will unpair it.

## Note

In case you encounter this pop-up, always ignore it. It will not affect the pairing process.
![connection-request.png](images/connection-request.png)
