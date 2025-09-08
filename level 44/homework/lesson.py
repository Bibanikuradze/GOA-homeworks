# 1:
def reverse_seq(n):
    return list(range(n, 0, -1))


# 2:
def rps(p1, p2):
    if p1 == p2:
        return "draw!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "player 1 won!"
    else:
        return "player 2 won!"
    

# 3:
def is_divisible(n, x, y):
    return n % x == n % y == 0


# 4:
def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep

# 5:
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"