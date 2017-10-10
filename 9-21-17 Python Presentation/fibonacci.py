#!/usr/bin/env python3


def fibonacci(start=(0, 1)):
    '''
    Generator for an infinite fibonacci series
    starting with the pair of values passed to start
    '''
    a, b = start
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    import time
    for n in fibonacci():
        print(n)
        time.sleep(1)
