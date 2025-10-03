# RSAnalyze
&emsp;RSAnalyze is a lightweight app built for exploring RSA cryptography. Featuring a simple, user-friendly GUI that lets users calculate RSA keys from custom or randomized primes. RSAnalyze also includes built-in integer factorization using Pollard’s Rho algorithm, displaying the factors along with the computation time.

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Greenest-Guy/RSAnalyze/total?style=for-the-badge&color=029cff) ![GitHub Release](https://img.shields.io/github/v/release/Greenest-Guy/RSAnalyze?style=for-the-badge&color=029cff)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/Greenest-Guy/RSAnalyze?style=for-the-badge)](https://www.codefactor.io/repository/github/Greenest-Guy/RSAnalyze)

  
## :mag: Preview
![preview](https://github.com/Greenest-Guy/RSAnalyze/blob/main/preview.png)

## :star2: Features
### - Custom or Randomized prime values
### - Windows & MacOS Support
### - Built-in Integer Factorization (Pollard's Rho)
### - Real-Time Output
### - Lightweight & Open-Sourced

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
&emsp; The Pollard's rho algorithm is automatically implemented within RSAnalyze to both demonstrate the security (or lack thereof) in RSA keys of varying p & q sizes. The program outputs the computation time, calculated factors, and the number of iterations taken to factorize. To learn more about how the Factorization works, please take a look at my Pollard's rho repository here [`Pollard's Rho`](https://github.com/Greenest-Guy/Pollards-Rho-Python).

![image](https://github.com/Greenest-Guy/RSAnalyze/blob/main/PolloardsRho_snapshot.png)



## :arrow_heading_down: Download Options (Windows & MacOS)
### :octocat: GitHub
- [Download Latest Release](https://github.com/Greenest-Guy/RSAnalyze/releases/latest)
### :snake: Source Code
1. Clone the repository and install all dependencies via pip
2. Run main.py using Python version 3.7+
