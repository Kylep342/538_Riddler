#!/usr/bin/env python

import datetime

def main():
    day = datetime.date.today()
    palindrome_dates = []
    for offset in range((datetime.date(2100, 1, 1) - day).days):
        if day.strftime("%m%d%Y") == day.strftime("%m%d%Y")[::-1]:
            palindrome_dates.append(day.strftime("%m/%d/%Y"))
        day += datetime.timedelta(days=1)
    print(f'The {len(palindrome_dates)} palindrome dates remaining in this century are:\n{palindrome_dates}')


if __name__ == '__main__':
    main()

