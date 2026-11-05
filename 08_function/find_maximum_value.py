#Find Maximum Value
def get_max(*num): 
    if len(num) == 0:
        return None 
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n 
    return max_num
print(get_max(3,12,32,9,123,21))
print(get_max('arush','Payal','zarina','Yogesh','yogiraj')) 