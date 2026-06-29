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




machine=VendingMachine(5,1000)

machine.buy(2,5000)
