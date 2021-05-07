import sys
import glob
from PIL import Image


"""
Usage:
python crop.py l
python crop.pt r
Here, 'l' is for left display and 'r' is for right display.

When there are 2 displays connected and you try to take a screenshot,
the screenshot combines both the displays.

This script crops and saves the left half of the image.
"""

# Defined ratio of the source image
RATIO = [3840 / 1080, 3286 / 1080]

# Width of the left display is the divider of the 2 displays.
DIVIDER = 1366


def crop_image(file_name, display):

    # Open the image in RGB mode
    im = Image.open(file_name)

    # Size of the image in pixels
    width, height = im.size

    # Checking the ratio
    ratio = width / height
    if ratio in RATIO:
        # Setting the points to keep the first half of the image
        # Settings for left display
        if display == 'l':
            left = 0
            top = 0
            right = DIVIDER
            bottom = height

        # Settings for right display
        if display == 'r':
            left = DIVIDER
            top = 0
            right = width
            bottom = height

        # Crop the image
        im1 = im.crop((left, top, right, bottom))

        # Shows the image in image viewer
        # im1.show()
        # Saving the file
        im1.save(file_name)
    else:
        print("Ratio doesn't meet the requirements.")


if __name__ == '__main__':
    min_args = 1
    max_args = 1
    argv = sys.argv[1:]
    expected_values = ['l', 'r']

    if len(argv) < min_args:
        if min_args == 1:
            print(f"Please enter at least {min_args} argument.")
        else:
            print(f"Please enter at least {min_args} arguments.")
        sys.exit()

    if len(argv) > max_args:
        if max_args == 1:
            print(f"Please enter exactly {max_args} argument.")
        else:
            print(f"Please enter exactly {max_args} arguments.")
        sys.exit()

    display = argv[0].lower()
    if display not in expected_values:
        print(f"Please enter a valid value from: {expected_values}")
        sys.exit()

    image_files = glob.glob('*.png')
    if image_files:
        for file_name in image_files:
            crop_image(file_name, display)
        print("SUCCESS: Operation completed.")
    else:
        print("INFO: No image file to crop.")
