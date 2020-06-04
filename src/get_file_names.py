"""
A python script to show all the file names inside the directory recursively,
as well as get it in the clipboard.

Usage:
python get_file_names.py 'directory_path'
Note: Make sure to pass the path within ''

If no argument is passed, it will consider the present directory where the
app is located.
"""
import os
import sys
import pyperclip


script_name = __file__.split('\\')[-1:][0]

if len(sys.argv) == 1:
    path = '.'
else:
    path = sys.argv[1]
    path = path.replace('\\', '/')


def main():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file != script_name:
                # file_name = os.path.join(r, file)
                files.append(file)

    # Writing all file names into a string to paste in the clipboard
    string = ''
    for file in files:
        string = string + file + '\n'

    pyperclip.copy(string)
    pyperclip.paste()

    print(string)


if __name__ == '__main__':
    main()
