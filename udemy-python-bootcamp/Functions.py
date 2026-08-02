

'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
'''
def spy_game(nums):
    #007 order list
    code = [0,0,7]
    # position in the above code list
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

**************************************************************************************************************************************************************************

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

**************************************************************************************************************************************************************************

