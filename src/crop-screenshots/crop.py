import glob
from PIL import Image

"""
When there are 2 displays connected and you try to take a screenshot,
the screenshot combines both the displays.

This script crops and saves the left half of the image.
"""

# Defined ratio of the source image
RATIO = [3840 / 1080, 3286 / 1080]


def crop_image(file_name):
    # Open the image in RGB mode
    im = Image.open(file_name)

    # Size of the image in pixels
    width, height = im.size

    # Checking the ratio
    ratio = width / height
    if ratio in RATIO:
        # Setting the points to keep the first half of the image
        left = 0
        top = 0
        right = width/2
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
    image_files = glob.glob('*.png')
    if image_files:
        for file_name in image_files:
            crop_image(file_name)
        print("SUCCESS: Operation completed.")
    else:
        print("INFO: No image file to crop.")
