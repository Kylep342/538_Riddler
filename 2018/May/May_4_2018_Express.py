#!/usr/bin/env python


def assemble_number_from_digits(digits_list):
    number = 0
    for pos in range(len(digits_list)):
        number += digits_list[pos] * 10 ** (len(digits_list) - (pos + 1))
    return number


def express():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        if a != b != c != d != e and assemble_number_from_digits([a, b, c, c, d, e]) * 4 == assemble_number_from_digits([e, d, c, c, b, a]):    
                            print('a: {0}, b: {1}, c: {2}, d: {3}, e: {4}'.format(a, b, c, d, e))


if __name__ == '__main__':
    express()
