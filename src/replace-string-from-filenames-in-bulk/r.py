import os

script_name = __file__.split('\\')[-1:][0]
path = '.'

file_formats = 'mp4 mkv'
old_string = ' - youtube'
new_string = ''

# Create a list like ['mp4', 'mkv', 'avi']
file_formats = file_formats.split(' ')


def get_new_file_name(file_name):
    file_name = file_name.lower()
    for file_format in file_formats:
        if file_name.endswith(file_format):
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
                print(file_name, new_file_name)
                rename(file_name, new_file_name)


if __name__ == '__main__':
    main()
