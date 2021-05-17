import datetime
from fpdf import FPDF


def format_date(date):
    """Format the date as DD-MM-YYYY."""

    return date.strftime("%d-%m-%Y")


def generate(persons, start_date, days, interval):
    """Generate the output."""

    data = []

    start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y").date()
    end_date = start_date + datetime.timedelta(days)  # Find the end date.

    # text = "Cleaning Schedule\n"

    # Table header
    data.append(['Date', 'Name', 'Kitchen', 'WC'])

    present_date = start_date
    index = 0
    while present_date <= end_date:
        date = format_date(present_date)
        person = persons[index]
        data.append([date, person, '[  ]', '[  ]'])

        # Add the interval to the present date.
        present_date += datetime.timedelta(interval)

        # Change the person.
        index += 1
        if index > len(persons) - 1:
            index = 0

    return data


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


def generate_pdf(data):
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    spacing = 2

    pdf.set_font("Arial", size=16)
    pdf.cell(w=0, h=20, txt='Cleaning Schedule', ln=1, align='C')

    pdf.set_font("Arial", size=12)
    for row in data:
        for item in row:
            pdf.cell(w=col_width, h=row_height*spacing,
                     txt=item, border=1, align='C')
        pdf.ln(row_height*spacing)

    pdf.output('clean.pdf')


if __name__ == "__main__":
    # generate(*take_input())
    persons = ['Smith', 'Ben']
    start_date = '09-05-2021'
    days = 120
    interval = 7
    test_data = (persons, start_date, days, interval)
    data = generate(*test_data)
    generate_pdf(data)
