# 1)
def manual_list(start, end, step, user_num):
    return[i for i in range(start,end,step) if i > user_num] 
print(manual_list(1, 20, 2, 10))
print(manual_list(5, 50, 5, 25))
print(manual_list(10, 100, 10, 50))



# 2)
list9 = [i for i in range(1,101) if (i%3 == 0 or i%5 == 0) and i%15 != 0]
print(list9)



# 3)
list10 = [i for i in range(10,201) if str(i) == str(1)[::-1]]
print(list10)