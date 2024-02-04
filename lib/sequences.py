#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]
    if length > 2:
        for i in range(length - 2):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    elif length == 1:
        fibonacci.pop()
    elif length == 0:
        fibonacci.clear()
    print(fibonacci)