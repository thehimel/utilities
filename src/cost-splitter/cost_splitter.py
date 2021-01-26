import sys
from datetime import datetime

"""
Cost splitter between 2 persons.

Usage:
python cost_splitter.py <1st_person_amount> <2nd_person_amount>
python cost_splitter.py 20 20
python cost_splitter.py 30 10
python cost splitter.py 40 20
python cost splitter.py 12.09 2.95
"""


def print_write(text):
    print(text)

    with open("cost_splitter_data.txt", "a") as file_object:
        file_object.write("\n" + text)


def main(argv):
    if len(argv) != 2:
        print("INFO: Please pass 2 arguments.")
        sys.exit()

    first = float(argv[0])
    second = float(argv[1])

    total_half = (first+second)/2

    print_write("\n-----------------------------------")
    # dd/mm/YY H:M:S
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print_write(f"Date and Time: {dt_string}")
    print_write(f"Amount spent by 1st person: {first:.2f}")
    print_write(f"Amount spent by 2nd person: {second:.2f}")
    print_write(f"Total expenditure: {(first + second):.2f}")
    print_write(f"Average expenditure: {((first + second)/2):.2f}")

    if second < total_half:
        print_write(
            f"2nd person gives 1st person: {(total_half - second):.2f}")
    elif first < total_half:
        print_write(f"1st person gives 2nd person: {(total_half - first):.2f}")
    else:
        print_write("Both costs are same.")
    print_write("-----------------------------------")


if __name__ == "__main__":
    main(sys.argv[1:])
