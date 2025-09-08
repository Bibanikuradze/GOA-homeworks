# 1

def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res

# 2)

def get_age(age):
    return int(age[0])

# 3)

def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]

# 4)

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

# 5)

def check_for_factor(base, factor):
    return base % factor == 0