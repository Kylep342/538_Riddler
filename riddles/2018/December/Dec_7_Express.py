"""
Riddler Express - December 7, 2018

From Josh Vandenham, precipitation permutations:

Louie walks to and from work every day. In his city, there is a 50
percent chance of rain each morning and an independent 40 percent
chance each evening. His habit is to bring (and use) an umbrella if
it’s raining when he leaves the house or office, but to leave them all
behind if not. Louie owns three umbrellas.

On Sunday night, two are with him at home and one is at his office.
Assuming it never starts raining during his walk to his home or office,
what is the probability that he makes it through the work week without
getting wet?

Solution by Kyle Pekosh https://github.com/Kylep342
"""

import argparse
import random


def rain_forecast(weights):
    """
    Function to determine if it will rain.

    Arguments:
        weights [list[float]]:
            2 item list with decimal weights representing [P(no rain), P(rain)]

    Returns:
        boolean [bool]:
            Boolean representing presence of rain
    """
    return random.choices([False, True], weights)[0]


def walk(weights, start_umbrellas, end_umbrellas):
    """
    Function to simulate Louie making a single commute

    Arguments:
        weights [list[float]]:
            2 item list with decimal weights representing [P(no rain), P(rain)]
        start_umbrellas [list[int]]:
            A list representing a collection of umbrellas at a starting point
        end_umbrellas [list[int]]:
            A list representing a collection of umbrellas at an ending point

    Returns:
        boolean [bool]:
            A boolean representing Louie's status as dry

    """
    forecast = rain_forecast(weights)
    if forecast:
        try:
            louie = start_umbrellas.pop()
        except IndexError:
            return False
        else:
            end_umbrellas.append(louie)
            return True
    return True


def simulate_week():
    """
    Function to simulate Louie's commute for one week

    Arguments:
        none

    Returns:
        0 if Louie gets rained on
        1 if Louie remains dry
    """
    home_umbrellas = [1, 1]
    work_umbrellas = [1]
    am_weights = [.5, .5]
    pm_weights = [.6, .4]
    for i in range(5):
        dry_morning = walk(am_weights, home_umbrellas, work_umbrellas)
        if not dry_morning:
            return 0
        dry_evening = walk(pm_weights, work_umbrellas, home_umbrellas)
        if not dry_evening:
            return 0
    return 1


def main(weeks):
    """
    """
    dry_weeks = 0
    for week in range(weeks):
        dry_weeks += simulate_week()
    print(f'weeks: {weeks}\nDry Weeks: {dry_weeks}\nP(dry): {100 * (dry_weeks/weeks):.4f}%')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--weeks', type=int, default=100000, help='Number of weeks to simulate')
    args = parser.parse_args()
    main(args.weeks)
