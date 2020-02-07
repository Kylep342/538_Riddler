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


# prints (as of 02/07/2020):
# The 8 palindrome dates remaining in this century are:
# ['12/02/2021', '03/02/2030', '04/02/2040', '05/02/2050', '06/02/2060', '07/02/2070', '08/02/2080', '09/02/2090']
