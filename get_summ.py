def get_summ(one, two, delimiter='&'):
    res_str = f'{one}{delimiter}{two}'
    return res_str.upper()


result = get_summ('learn','pr')
print(result)