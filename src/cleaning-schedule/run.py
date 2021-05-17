import datetime


def format_date(date):
    """Format the date as DD-MM-YYYY."""

    return date.strftime("%d-%m-%Y")


def add_to_file(file_obj, text):
    """ Appends a text to the file."""

    file_obj.writelines(text + '\n')


def generate(persons, start_date, days, interval):
    """Generate the output."""

    file_name = "clean.txt"
    file_obj = open(file_name, "w")

    start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").date()
    end_date = start_date + datetime.timedelta(days)  # Find the end date.

    # create a cell
    text = "Cleaning Schedule\n"
    add_to_file(file_obj, text)

    # Table header
    text = (f"{'Date'.ljust(10)} {'Name'.center(10)} " +
            f"{'Kitchen'.center(8)}{'WC'.center(8)} ")

    add_to_file(file_obj, text)

    present_date = start_date
    index = 0
    while present_date <= end_date:
        date = format_date(present_date)
        person = persons[index]
        text = (f"{date.ljust(10)} {person.center(10)} " +
                f"{'[ ]'.center(8)} {'[ ]'.center(8)}")
        add_to_file(file_obj, text)

        # Add the interval to the present date.
        present_date += datetime.timedelta(interval)

        # Change the person.
        index += 1
        if index > len(persons) - 1:
            index = 0

    file_obj.close()


def take_input():
    person_count = int(input("Number of persons = "))
    persons = []

    n = 0
    while n < person_count:
        name = input(f"Name of person {n+1} = ")
        persons.append(name)
        n += 1

    start_date = input("Start date (DD-MM-YYYY) = ")
    days = int(input("Number of days = "))
    interval = int(input("Interval in days = "))

    return persons, start_date, days, interval


if __name__ == "__main__":
    # generate(*take_input())
    persons = ['Smith', 'Ben ']
    start_date = '09-05-2021'
    days = 120
    interval = 7
    generate(persons, start_date, days, interval)
