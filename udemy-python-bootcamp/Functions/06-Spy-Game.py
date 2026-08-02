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
