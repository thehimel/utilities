import sys
import glob
from PIL import Image


"""
Usage:
python resize.py height width
python resize.py 1920 1080

The script crops the image according to the given resolution.
"""


def resize_image(file_name, width, height):

    # Open the image in RGB mode
    im = Image.open(file_name)

    # Size of the image in pixels
    im_width, im_height = im.size

    if im_width <= width and im_height <= height:
        print("INFO: Ratio doesn't meet the requirements.")
        return

    left, top, right, bottom = 0, 0, width, height
    
    if im_width > width:
        left = im_width/2 - width/2
        right = im_width/2 + width/2

    if im_height > height:
        buffer = 48 # There is a buffer for some systems
        top = im_height/2 - height/2 - buffer
        bottom = im_height/2 + height/2 - buffer

    # Crop the image
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    # im1.show()
    # Saving the file
    im1.save(file_name)


if __name__ == '__main__':
    args_count = 2
    argv = sys.argv[1:]

    if len(argv) < args_count or len(argv) > args_count:
        print(f"ERROR: Please enter exactly {args_count} argument.")
        sys.exit()

    first, second = int(argv[0]), int(argv[1])
    res = (first, second) if first > second else (second, first)
    print(*res)


    image_files = glob.glob('*.png')
    if image_files:
        for file_name in image_files:
            resize_image(file_name, *res)
        print("SUCCESS: Operation completed.")
    else:
        print("INFO: No image file to crop.")
