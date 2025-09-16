# Pollard's Rho Algorithm for Integer Factorization
from customtkinter import *
import random
import time
import math


class PollardsRho:
    def __init__(self, num, textbox=None):
        self.num = num
        self.textbox = textbox

        if self.textbox != None:
            self.textbox.delete("0.0", "end")

    def factorize(self):
        iteration = 0
        start_time = time.perf_counter()

        if self.num <= 0:
            raise ValueError("Number must be a positive integer")
        if self.num == 1:
            return 1
        if self.num % 2 == 0:
            return 2

        x = random.randint(2, self.num - 1)
        y = x
        c = random.randint(1, self.num - 1)
        d = 1

        while d == 1:
            x = (pow(x, 2, self.num) + c) % self.num

            y = (pow(y, 2, self.num) + c) % self.num
            y = (pow(y, 2, self.num) + c) % self.num

            d = math.gcd(abs(x - y), self.num)

            iteration += 1

            if self.textbox != None:
                self.textbox.insert(0.0, f"iter: {iteration}\n")

        if self.textbox != None:
            end_time = time.perf_counter()

            elapsed_time = end_time - start_time

            self.textbox.insert(
                0.0, f"\nFactorization Time: {round(elapsed_time, 6)} seconds\n")

            self.textbox.insert(0.0, f"n = {d} * {self.num // d}\n")

        return d
