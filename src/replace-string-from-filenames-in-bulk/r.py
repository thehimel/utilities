
"""
A python script to replace a particular string from the file names in all files
of the current directory recursively.
It will enter into all directories from the given directory.

Usage:
python get_file_names.py 'directory_path'
Note: Make sure to pass the path within ''

If no argument is passed, it will consider the present directory where the
app is located.

Note:
When comparing the endswith fileformat, it may be possible that the format in
the file is in capital form. E.g. File Name.MKV. Thus, where comparing
the file format, we need to consider the lowercase of the the file name.
"""
import os
import sys

script_name = __file__.split('\\')[-1:][0]

if len(sys.argv) == 1:
    path = '.'
else:
    path = sys.argv[1]
    path = path.replace('\\', '/')

file_formats = 'mp4 mkv'
old_string = ' - YouTube'
new_string = ''

# Create a list like ['mp4', 'mkv', 'avi']
file_formats = file_formats.split(' ')


def get_new_file_name(file_name):
    for file_format in file_formats:
        if file_name.lower().endswith(file_format):
            new_file_name = file_name.replace(old_string, new_string)
            return new_file_name

    return file_name


def rename(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
    except OSError as e:
        print("Error:", e)


def main():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file != script_name:
                file_name = os.path.join(r, file)
                new_file_name = os.path.join(r, get_new_file_name(file))
                if new_file_name != file_name:
                    rename(file_name, new_file_name)
                    print(file_name, new_file_name)


if __name__ == '__main__':
    main()
