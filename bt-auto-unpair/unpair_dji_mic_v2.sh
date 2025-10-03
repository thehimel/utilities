#!/bin/bash

# Source profile to get Homebrew PATH
source ~/.zshrc 2>/dev/null || source ~/.bash_profile 2>/dev/null || true

# Must be in uppercase
DEVICE_MAC="58-B8-58-0B-06-57"

echo "$(date): Monitoring device $DEVICE_MAC..."

# Track previous connection state
PREVIOUS_STATUS=""

while true; do
    # Check if device is connected (1 = connected, 0 = disconnected)
    CURRENT_STATUS=$(blueutil --is-connected "$DEVICE_MAC")
    
    # Check if device is paired (exists in paired devices list)
    IS_PAIRED=$(blueutil --paired | grep -i "$DEVICE_MAC" | wc -l)

    # Only unpair if device was previously connected and is now disconnected AND is currently paired
    if [ "$PREVIOUS_STATUS" = "1" ] && [ "$CURRENT_STATUS" = "0" ] && [ "$IS_PAIRED" -gt 0 ]; then
        echo "$(date): Device was paired and connected, now disconnected. Unpairing..."

        # Unpair device via blueutil
        blueutil --unpair "$DEVICE_MAC"

        echo "$(date): Device unpaired."
    fi
    
    # Update previous status for next iteration
    PREVIOUS_STATUS="$CURRENT_STATUS"
    
    sleep 5
done
