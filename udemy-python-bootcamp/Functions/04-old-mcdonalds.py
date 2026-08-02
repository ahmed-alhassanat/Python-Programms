

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
