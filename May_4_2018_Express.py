#!/usr/bin/env python

def letters_numbers():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        if a != b != c != d != e and (int(str(a) + str(b) + str(c) + str(c) + str(d) + str(e)) * 4 == int(str(e) + str(d) + str(c) + str(c) + str(b) + str(a))):
                                print('a: {0}, b: {1}, c: {2}, d: {3}, e: {4}'.format(a, b, c, d, e))


if __name__ == '__main__':
    letters_numbers()
