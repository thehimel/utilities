#!/bin/bash

# Must be in uppercase
DEVICE_MAC="58-B8-58-0B-06-57"

echo "$(date): Monitoring device $DEVICE_MAC..."

while true; do
    # Check if device is connected (1 = connected, 0 = disconnected)
    STATUS=$(blueutil --is-connected "$DEVICE_MAC")

    if [ "$STATUS" = "0" ]; then
        echo "$(date): Device disconnected. Unpairing..."

        # Unpair device via blueutil
        blueutil --unpair "$DEVICE_MAC"

        echo "$(date): Device unpaired."
    fi
    sleep 5
done
