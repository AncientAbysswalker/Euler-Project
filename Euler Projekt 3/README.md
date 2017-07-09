# Even Fibonacci numbers

## Problem Statement
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

## Solution
This problem is essentially just finding the factors of a natural number. Every natural number is either a prime number itself or a product of multiple prime numbers. My logic here is relatively simple - I try to divide the given number by each sequential prime until the remainder is no longer 0. What I mean by this is if I divide a numer by a prime, if the remainder is 0 it is divisible by that prime, if it is not 0 then we can try the next, higher prime. Now the fun thing here is that I figured out (hadn't really thought about this before) that if you divide a number by a prime and the result is less than the previous prime (the prime before the one we are currently trying) then the number is a prime number.




ef checkPrime(number,Primes):
    for Prime in Primes:
        if number%Prime == 0:
            return False
    return True

#Problem definition
N=600851475143 #4*13195
P=[2]
F=[]

#Sum to upper limit
Factorized=False
while not Factorized:
    [tempQuotient,tempRemainder]=(divmod(N,P[-1]))
    if tempRemainder==0:
        F.append(P[-1])
        N=tempQuotient
    else:
        tmpC=P[-1]
        while True:
            tmpC+=1
            if checkPrime(tmpC,P):
                P.append(tmpC)
                break
            else:
                if N/tmpC<P[-1]:
                    if N!=1: F.append(N)
                    Factorized=True
                    break
print("Prime Factors are:" + str(F))



This problem is relatively straight-forward. Fibonacci sequence numbers follow a consistent pattern, with every third number being even after the first two numbers 1 and 2. This means that <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{F}_{i&plus;1}&space;=&space;\mathcal{F}_{i}&plus;\mathcal{F}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{F}_{i&plus;1}&space;=&space;\mathcal{F}_{i}&plus;\mathcal{F}_{i-1}" title="\mathcal{F}_{i+1} = \mathcal{F}_{i}+\mathcal{F}_{i-1}" /></a> with the even elements corresponding to <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{F}_{1&plus;3n},&space;n\epsilon&space;\mathbb{Z}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{F}_{1&plus;3n},&space;n\epsilon&space;\mathbb{Z}" title="\mathcal{F}_{1+3n}, n\epsilon \mathbb{Z}" /></a> if the numbers 1 and 2 are elements 0 and 1 respective.

I simply made a fibonacci class object that stores the current value in the sequence, past value in the sequence, and a counter for determining if it is even or odd.
