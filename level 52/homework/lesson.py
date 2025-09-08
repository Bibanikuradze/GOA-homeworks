def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        prev_num = arr[i-1]
        
        if cur_num - prev_num > 1: return cur_num
    
    return None




def to_alternating_case(string):
    return string.swapcase()





def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")





def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]





def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary*10}"
    return f"${salary}"




def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    elif exam > 75 and projects >= 5: return 90
    elif exam > 50 and projects >= 2: return 75
    return 0





def sum_str(a, b):
    if len(a) > 0 and len(b) == 0: return a
    elif len(a) == 0 and len(b) > 0: return b
    elif len(a) == 0 and len(b) == 0: return "0"

    return str(int(a) + int(b))