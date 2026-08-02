
********************************************************************************************************************************************



**************************************************************************************************************************************************************************

"""
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.
"""
def myfunc(string):
    result = ""
    cnt = 0
    for i in string:
        cnt += 1
        if cnt%2 == 0:
           result += i.upper() 
        else:
            result += i
        
    return result


""" 
string_list = []
cnt = 0
for i in string:
    string_list.append(i)
    cnt +=1
print (string_list)
print(cnt)
""" 


**************************************************************************************************************************************************************************

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a  string
'''

def old_macdonald(name):
    if len(name) > 3:
        name_list = list(name)
        name_list[0] = name_list[0].capitalize()
        name_list[3] = name_list[3].capitalize()
        name_new = ''.join(name_list)
    else:
        return 'Name is too short!'
    return name_new

**************************************************************************************************************************************************************************

'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
'''
def master_yoda(text):
    text_split = text.split()
    text_list = list(text_split)
    text_list.reverse()
    text_new = " ".join(text_list)
    return text_new

**************************************************************************************************************************************************************************

'''
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

'''
def has_33(nums):
    for i in range (0, len(nums)-1):
        return (nums[i] == 3 and nums[i+1] == 3  )

**************************************************************************************************************************************************************************

'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
'''
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result

**************************************************************************************************************************************************************************

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

