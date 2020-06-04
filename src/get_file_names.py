import os
import sys

script_name = __file__.split('\\')[-1:][0]

if len(sys.argv) == 1:
    path = '.'
else:
    path = sys.argv[1]
    path = path.replace('\\', '/')


def main():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file != script_name:
                file_name = os.path.join(r, file)
                print(file)


if __name__ == '__main__':
    main()
