# Pollard's Rho Algorithm for Integer Factorization
# Expected Time Complexity: O(sqrt(p))

import random
import math

class PollardsRho:
    def __init__(self, num):
        self.num = num

    def factorize(self):
        if self.num == 1:
            return 1
        
        elif self.num % 2 == 0:
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

            if d == self.num:
                return None

        return d
