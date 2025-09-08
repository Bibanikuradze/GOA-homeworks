def multiply(a, b):
    return a * b

def make_negative( number ):
    if number > 0:
        return number * -1
    else: return number

def make_negative( number ):
    if number > 0:
        return number * -1
    else:return number

def opposite(number):
    return number * -1

def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"
    
def positive_sum(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res

def repeat_str(repeat, string):
    res = ""
    for i in range(repeat):
        res = res + string
    return res

def square_sum(numbers):
    result=0
    for i in numbers:
        result+=i**2
    return result