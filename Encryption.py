import math
def encryption(s):
    if len(s) < 1:
        return ''
    sqrt_length_of_str = math.sqrt(len(s))
    rows = math.floor(sqrt_length_of_str)
    columns = math.ceil(sqrt_length_of_str)
    if rows * columns < len(s):
        rows+=1

    matrix = [['' for i in range(columns)] for j in range(rows)]
    
    for row in range(rows):
        for column in range(columns):
            if row*columns + column < len(s):
                matrix[row][column] = s[row*columns + column]
        
    result = ''
    for column in range(columns):
        if column > 0:
            result += ' '
        for row in range(rows):
            if matrix[row][column] != '':
                result+=matrix[row][column]
        
    return result

print(encryption(""))
print(encryption("a"))
print(encryption("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"))
print(encryption("haveaniceday"))
print(encryption("feedthedog"))
print(encryption("chillout"))