# RSAnalyze
&emsp;RSAnalyze is a lightweight app built for exploring RSA cryptography. Featuring a simple, user-friendly GUI that lets users calculate RSA keys from custom or randomized primes. RSAnalyze also includes built-in integer factorization using Pollard’s Rho algorithm, displaying the factors along with the computation time.

  
## :mag: Preview
![preview](https://github.com/Greenest-Guy/RSAnalyze/blob/main/preview.png)

## :star2: Features

## :1234: RSA Value Calculations

$$
p = \text{positive prime integer}
$$

$$
q = \text{positive prime integer} | p \neq q
$$

$$
n = p \cdot q
$$

$$
\varphi(n) = (p - 1)(q - 1)
$$

$$
1 < e < \varphi(n) \land \gcd(e, \varphi(n)) = 1
$$

$$
(e \cdot d) \bmod \varphi(n) = 1
$$



## :gear: Pollard's Rho Factorization
