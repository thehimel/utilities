from pynput import keyboard


def key_press(key):
    try:
        # Print the key that was pressed
        print(f'Key {key} pressed')

    except AttributeError:
        # Some special keys don't have attributes like char or name
        print(f'Special key {key} pressed')


# Create a listener for key events
listener = keyboard.Listener(on_press=key_press)

# Start listening for key presses
listener.start()

# Run the listener in the background
listener.join()
