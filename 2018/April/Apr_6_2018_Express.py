#!/usr/bin/env python

"""
Riddler Express puzzle from 4/6/2018
See https://fivethirtyeight.com/features/when-will-the-arithmetic-anarchists-attack/

Puzzle:
From Eric Veneto, mathematical madmen are on the loose:

The year is 2000, and an arithmetical anarchist group has an idea.
For the next 100 years, it will vandalize a famous landmark whenever
the year (in two-digit form, for example this year is “18”) is the
product of the month and date
(i.e. month × date = year, in the MM/DD/YY format).

A few questions about the lawless ensuing century:
How many attacks will happen between the beginning of 2001 and the end of 2099?
What year will see the most vandalism?
The least?
What will be the longest gap between attacks?
"""


import collections
import datetime


def determine_vandalism_dates():
    _vandalism_dates = []
    _c_begin = datetime.date(2001, 1, 1)
    _c_end = datetime.date(2099, 12, 31)
    for _day in range((_c_end - _c_begin).days + 1):
        _date = _c_begin + datetime.timedelta(_day)
        if _date.year % 2000 == _date.month * _date.day:
            _vandalism_dates.append(_date)
    return _vandalism_dates


def determine_max_gap(date_list):
    days_without_incident = 0
    _incident_1 = datetime.date.today()
    _incident_2 = datetime.date.today()
    for _atk_no in range(len(date_list) - 1):
        _days_between_attacks = (date_list[_atk_no + 1] - date_list[_atk_no]).days - 1
        if  _days_between_attacks > days_without_incident:
            _incident_1 = date_list[_atk_no]
            _incident_2 = date_list[_atk_no + 1]
            days_without_incident = _days_between_attacks
    return _incident_1, _incident_2, days_without_incident


def answer_Riddler():
    _vandalism_dates = determine_vandalism_dates()
    print("There will be {0} attacks in the 21st century.".format(len(_vandalism_dates)))
    _v_years = [_attack.year for _attack in _vandalism_dates]
    _atks_per_year = collections.Counter(_v_years)
    _worst_year = max(_atks_per_year, key=_atks_per_year.get)
    print("{0} will have the most attacks, with {1}.".format(_worst_year, _atks_per_year[_worst_year]))
    _21st_century = set(range(2001, 2100))
    _years_of_attacks = set(_v_years)
    _best_years = sorted(list(_21st_century.difference(_years_of_attacks)))
    print("The years with the fewest attacks are {0}, with 0.".format(_best_years))
    _d1, _d2, _peace = determine_max_gap(_vandalism_dates)
    print("The longest tenure of peacetime is {0} days, between {1} and {2}.".format(_peace, _d1, _d2))


if __name__ == '__main__':
    answer_Riddler()

# Output:
# There will be 212 attacks in the 21st century.
# 2024 will have the most attacks, with 7.
# The years with the fewest attacks are [2037, 2041, 2043, 2047, 2053, 2058, 2059, 2061, 2062, 2067, 2071, 2073, 2074, 2079, 2082, 2083, 2086, 2089, 2094, 2097], with 0.
# The longest tenure of peacetime is 1097 days, between 2057-03-19 and 2060-03-20.
