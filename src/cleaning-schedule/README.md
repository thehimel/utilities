# Cleaning Schedule

Generate cleaning schedule based on persons, start date, number of days, and interval.

## Python Libraries

* fpdf

## Usage

```output
$ python run.py -h
usage: run.py [-h] -p PERSONS [PERSONS ...] [-s START_DATE] [-d DAYS] [-i INTERVAL]

Generate cleaning schedule.

options:
  -h, --help            show this help message and exit
  -p PERSONS [PERSONS ...], --persons PERSONS [PERSONS ...]
                        Names of the person(s) separated by space.
  -s START_DATE, --start_date START_DATE
                        Starting date in format 'DD-MM-YYYY'. Default = Today
  -d DAYS, --days DAYS  Number of days. Default = 180
  -i INTERVAL, --interval INTERVAL
                        Cleaning interval in days. Default = 7
```

## Example Commands

```shell
python run.py -p Smith Ben
python run.py -p Smith Ben -s 01-01-2022 -d 180 -i 7
```

## Resources

* [Specify Date format for Python argparse Input Arguments](https://stackoverflow.com/questions/25470844/specify-date-format-for-python-argparse-input-arguments)
* [Black Configuration Format](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-format)
