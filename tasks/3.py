#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def check():
    s = 1

    while True:
        num = int(input("Введите число: "))
        if num == 0:
            print(f'Результат: {s}')
            break
        s *= num
        

if __name__ == '__main__':
    check()
