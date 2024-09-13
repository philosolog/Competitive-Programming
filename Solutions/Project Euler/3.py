import math

n = 600851475143

def primeFactors(n): # Note: This is better than Sieve on memory
    while n % 2 == 0:
        print(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            print(i)
            n = n // i
            
    if n > 2:
        print(n)
         
primeFactors(n)

# TODO: Review