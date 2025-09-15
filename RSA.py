from sympy import isprime, nextprime
import math


class RSA:
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
        if FERMAT < self.phi_n and self.iscoprime(self.phi_n, FERMAT):
            self.e = FERMAT

        else:
            self.e = self.find_coprime(self.phi_n)

        # Calculate d
        self.d = pow(self.e, -1, self.phi_n)

    @staticmethod
    def iscoprime(a, b):
        return math.gcd(a, b) == 1

    @staticmethod
    def find_coprime(phi_n):
        e = 3

        while e < phi_n:
            if math.gcd(e, phi_n) == 1:
                return e
            e += 2

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

    def get_values(self):
        return self.n, self.phi_n, self.e, self.d
