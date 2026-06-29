#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:

    def __init__(self, num_items, item_price):
        self.items = num_items
        self.price = item_price

    def buy(self, req_items, money):

        if req_items > self.items:
            raise ValueError("Not enough items in the machine")

        cost = req_items * self.price

        if money < cost:
            raise ValueError("Not enough coins")

        self.items -= req_items

        return money - cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())

    for _ in range(n):
        num_items, num_coins = map(int, input().split())

        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")

        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()