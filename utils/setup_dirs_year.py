"""
"""

import argparse
import os


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def setup_dir(base_path, year):
    base = os.path.join(base_path, year)
    if not os.path.isdir(base):
        os.mkdir(base)
        for month in MONTHS:
            os.mkdir(os.path.join(base, month))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', help="Year to make directories for")
    parser.add_argument('-b', '--base_path', help="Root path to build directories from")
    args = parser.parse_args()
    setup_dir(args.base_path, args.year)
