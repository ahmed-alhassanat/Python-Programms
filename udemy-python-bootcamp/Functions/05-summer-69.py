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

