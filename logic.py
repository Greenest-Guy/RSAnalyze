from sympy import isprime
import math


class Logic:
    def __init__(self, p, q):
        if not (isprime(p) and isprime(q)):
            raise ValueError("p and q must be prime")

        FERMAT = 65537

        # Calculate n and phi(n)
        self.p = p
        self.q = q
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)

        # Calculate e
        self.e = FERMAT if (self.phi_n > FERMAT and self.iscoprime(
            self.phi_n, FERMAT)) else 3

        if self.e != FERMAT:
            while not self.iscoprime(self.e, self.phi_n):
                self.e += 2

        # Calculate d
        self.d = pow(self.e, -1, self.phi_n)

    @staticmethod
    def iscoprime(a, b):
        return math.gcd(a, b) == 1

    def get_p(self):
        return self.p

    def get_q(self):
        return self.q

    def get_n(self):
        return self.n

    def get_e(self):
        return self.e

    def get_d(self):
        return self.d

    def get_eulers_totient(self):
        return self.phi_n

    def get_public_key(self):
        return (self.n, self.e)

    def get_private_key(self):
        return (self.n, self.d)
