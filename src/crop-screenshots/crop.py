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

This script crops and saves the left or right screen.
"""

# Defined ratio of the source image
RATIO = [3840 / 1080, 3286 / 1080, 5760 / 2160]

# Width of the left display is the divider of the 2 displays.
DIVIDER = 1920


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
        print("INFO: Ratio doesn't meet the requirements.")


if __name__ == '__main__':
    args_count = 1
    max_args = 1
    argv = sys.argv[1:]
    expected_values = ['l', 'r']

    if len(argv) < args_count or len(argv) > args_count:
        print(f"ERROR: Please enter at least {args_count} argument.")
        sys.exit()

    display = argv[0].lower()
    if display not in expected_values:
        print(f"ERROR: Please enter a valid value from: {expected_values}")
        sys.exit()

    image_files = glob.glob('*.png')
    if image_files:
        for file_name in image_files:
            crop_image(file_name, display)
        print("SUCCESS: Operation completed.")
    else:
        print("INFO: No image file to crop.")
