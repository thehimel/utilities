"""
Generate cleaning schedule based on persons, start date, number of days, and interval.
"""

from string import punctuation
from datetime import datetime, timedelta
from argparse import ArgumentParser, ArgumentTypeError
from fpdf import FPDF


def format_date(date: datetime.date) -> str:
    """
    Convert date object to string with format 'DD-MM-YYYY'.

    :param date: Date as datetime object.
    :return: Date in string type.
    """

    return date.strftime("%d-%m-%Y")


def generate(persons: list, start_date: datetime.date, days: int, interval: int) -> list[list]:
    """
    Generate the output.

    :param persons: Name(s) of the person(s).
    :param start_date: Starting date.
    :param days: Number of days.
    :param interval: Cleaning interval.
    :return: List of data.
    """

    persons = [person.strip(punctuation).capitalize() for person in persons]
    data = []
    end_date = start_date + timedelta(days)  # Find the end date.
    data.append(["Date", "Bin", "Kitchen and WC"])  # Table header.
    present_date = start_date
    bin_index = kwc_index = count = 0

    while present_date <= end_date:
        date = format_date(present_date)
        bin_person = persons[bin_index]
        if count % 2 == 0:
            kitchen = f"{persons[kwc_index]} [  ]"
            kwc_index += 1
            if kwc_index > len(persons) - 1:
                kwc_index = 0
        else:
            kitchen = ""
        data.append([date, f"{bin_person} [  ]", kitchen])
        present_date += timedelta(interval)
        bin_index += 1
        if bin_index > len(persons) - 1:
            bin_index = 0
        count += 1

    return data


def generate_pdf(data: list[list]) -> None:
    """
    Generate the pdf file.

    :param data: List of data.
    """
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    spacing = 2

    pdf.set_font("Arial", size=16)
    pdf.cell(w=0, h=20, txt="Cleaning Schedule", ln=1, align="C")

    pdf.set_font("Arial", size=12)
    for row in data:
        for item in row:
            pdf.cell(w=col_width, h=row_height * spacing, txt=item, border=1, align="C")
        pdf.ln(row_height * spacing)

    pdf.output("clean.pdf")


def valid_date(date: str) -> [datetime, ValueError]:
    """Get a date if the string is passed in valid format, else raise error.

    :param date: Starting date in format 'DD-MM-YYYY'.
    :return: Returns a date or raises error.
    """
    try:
        return datetime.strptime(date, "%d-%m-%Y").date()
    except ValueError as error:
        msg = f"Invalid date: {date}. Format: DD-MM-YYYY."
        raise ArgumentTypeError(msg) from error


if __name__ == "__main__":
    default_days, default_interval, today = 180, 7, datetime.now().date()
    parser = ArgumentParser(description="Generate cleaning schedule.")

    parser.add_argument(
        "-p",
        "--persons",
        nargs="+",
        type=str,
        help="Names of the person(s) separated by space.",
        required=True,
    )

    parser.add_argument(
        "-s",
        "--start_date",
        type=valid_date,
        default=today,
        help=f"Starting date in format 'DD-MM-YYYY'. Default = {format_date(today)} (Today)",
        required=False,
    )

    parser.add_argument(
        "-d",
        "--days",
        type=int,
        default=default_days,
        help=f"Number of days. Default = {default_days}",
        required=False,
    )

    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=default_interval,
        help=f"Cleaning interval in days. Default = {default_interval}",
        required=False,
    )

    args = parser.parse_args()
    generate_pdf(generate(args.persons, args.start_date, args.days, args.interval))
