#!/bin/bash

# Setup script for DJI Mic Auto-Unpair Service
# This script helps you install and manage the LaunchAgent

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_NAME="com.user.unpair-dji-mic.plist"
PLIST_FILE="$SCRIPT_DIR/$PLIST_NAME"
LAUNCHAGENTS_DIR="$HOME/Library/LaunchAgents"
TARGET_PLIST="$LAUNCHAGENTS_DIR/$PLIST_NAME"

case "$1" in
    install)
        echo "Installing DJI Mic Auto-Unpair service..."
        
        # Create LaunchAgents directory if it doesn't exist
        mkdir -p "$LAUNCHAGENTS_DIR"
        
        # Copy plist file to LaunchAgents directory
        cp "$PLIST_FILE" "$TARGET_PLIST"
        
        # Load the service
        launchctl load "$TARGET_PLIST"
        
        echo "✅ Service installed and started!"
        echo "The script will now run automatically at startup."
        echo ""
        echo "To check status: $0 status"
        echo "To stop: $0 stop"
        echo "To uninstall: $0 uninstall"
        ;;
        
    uninstall)
        echo "Uninstalling DJI Mic Auto-Unpair service..."
        
        # Unload the service
        launchctl unload "$TARGET_PLIST" 2>/dev/null
        
        # Remove the plist file
        rm -f "$TARGET_PLIST"
        
        echo "✅ Service uninstalled!"
        ;;
        
    start)
        echo "Starting DJI Mic Auto-Unpair service..."
        launchctl load "$TARGET_PLIST"
        echo "✅ Service started!"
        ;;
        
    stop)
        echo "Stopping DJI Mic Auto-Unpair service..."
        launchctl unload "$TARGET_PLIST"
        echo "✅ Service stopped!"
        ;;
        
    restart)
        echo "Restarting DJI Mic Auto-Unpair service..."
        launchctl unload "$TARGET_PLIST" 2>/dev/null
        launchctl load "$TARGET_PLIST"
        echo "✅ Service restarted!"
        ;;
        
    status)
        echo "Checking DJI Mic Auto-Unpair service status..."
        if launchctl list | grep -q "com.user.unpair-dji-mic"; then
            echo "✅ Service is running"
            echo ""
            echo "Recent logs:"
            echo "--- Output Log ---"
            tail -10 "$SCRIPT_DIR/unpair_dji_mic.log" 2>/dev/null || echo "No output log yet"
            echo ""
            echo "--- Error Log ---"
            tail -10 "$SCRIPT_DIR/unpair_dji_mic_error.log" 2>/dev/null || echo "No error log yet"
        else
            echo "❌ Service is not running"
        fi
        ;;
        
    logs)
        echo "Showing recent logs..."
        echo "--- Output Log ---"
        tail -20 "$SCRIPT_DIR/unpair_dji_mic.log" 2>/dev/null || echo "No output log yet"
        echo ""
        echo "--- Error Log ---"
        tail -20 "$SCRIPT_DIR/unpair_dji_mic_error.log" 2>/dev/null || echo "No error log yet"
        ;;
        
    *)
        echo "DJI Mic Auto-Unpair Service Manager"
        echo ""
        echo "Usage: $0 {install|uninstall|start|stop|restart|status|logs}"
        echo ""
        echo "Commands:"
        echo "  install   - Install and start the service (runs at startup)"
        echo "  uninstall - Remove the service completely"
        echo "  start     - Start the service"
        echo "  stop      - Stop the service"
        echo "  restart   - Restart the service"
        echo "  status    - Check if service is running and show recent logs"
        echo "  logs      - Show recent log output"
        echo ""
        echo "Example: $0 install"
        ;;
esac
