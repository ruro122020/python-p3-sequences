#!/usr/bin/env python3


def print_fibonacci(length):
    fib_list = []
    if length == 0:
        print(fib_list)
    elif length == 1:
        print([0])
    else:
        fib_list = [0, 1]
        while len(fib_list) < length:
            fib_list.append(fib_list[-1] + fib_list[-2])
        print(fib_list)

print_fibonacci(10)