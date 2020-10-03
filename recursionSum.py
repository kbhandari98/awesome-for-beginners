
def sum_numbers(y):
    if  y!= 0:
        y += sum_numbers(y-1)
    else:
        return 0
    return y

