#!/bin/bash

# Domain checker script
# Takes a list of domains and checks if they are registered or available

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/check_domain.py"
DEFAULT_DOMAINS_FILE="$SCRIPT_DIR/domains.txt"

# If no arguments provided, use default domains.txt file
if [ $# -eq 0 ]; then
    if [ ! -f "$DEFAULT_DOMAINS_FILE" ]; then
        echo "Error: domains.txt not found in $SCRIPT_DIR" >&2
        echo "Usage: $0 <domains_file>"
        echo "Or: $0 domain1.com domain2.com ..."
        exit 1
    fi
    set -- "$DEFAULT_DOMAINS_FILE"
fi

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: check_domain.py not found in $SCRIPT_DIR" >&2
    exit 1
fi

# Function to check a single domain
check_domain() {
    local domain="$1"
    python3 "$PYTHON_SCRIPT" "$domain"
}

# If first argument is a file, read from it
if [ -f "$1" ]; then
    # Read domains from file
    while IFS= read -r domain || [ -n "$domain" ]; do
        # Skip empty lines and comments
        domain=$(echo "$domain" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        if [ -z "$domain" ] || [[ "$domain" =~ ^# ]]; then
            continue
        fi
        check_domain "$domain"
    done < "$1"
else
    # Treat arguments as domain names
    for domain in "$@"; do
        check_domain "$domain"
    done
fi

