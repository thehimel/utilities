import os

script_name = __file__.split('\\')[-1:][0]
path = '.'

def main():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file != script_name:
                file_name = os.path.join(r, file)
                print(file)


if __name__ == '__main__':
    main()
