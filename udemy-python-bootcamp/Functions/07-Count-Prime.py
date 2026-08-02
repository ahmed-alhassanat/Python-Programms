'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
'''
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
           if x%y == 0:
               x += 1
               break
        else:
            primes.append(x)
            x+=1
    print(primes)
    return len(primes)
