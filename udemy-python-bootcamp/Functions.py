

'''
BLACKJACK: Given three integers between 1 and 11, 
if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
'''


def blackjack(a,b,c):
    if sum ((a,b,c)) <= 21:
        return sum ((a,b,c))
    elif sum ((a,b,c)) > 21 and 11 in (a,b,c):
        return sum((a,b,c)) -10
    else:
        return 'BUST!'


**************************************************************************************************************************************************************************

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9  (every 6 will be followed by at least one 9). Return 0 for no numbers.
'''
def summer_69(arr):
    #initalize total sum variable
    total = 0
    #flag to activate/deactivate the Add mode in the loop
    add = True
    #iterating through the numbers in the array loop
    for num in arr:
        #first while loop "Add mode"
        while add:
            if num != 6: 
                total += num
                break
            else:
                add = False
            
        #second while loop "Not Add Mode"
        while not add:
            if num !=9:
                break
            else:
                add= True
                break
    return total

**************************************************************************************************************************************************************************

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

