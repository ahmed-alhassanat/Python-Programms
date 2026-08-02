
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

