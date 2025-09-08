#შექმენით 3 ცვლადი, თითოეულში შეინახეთ მომხმარებლის შემოტანილი რიცხვი (გამოიყენეთ int ან float), შემდეგ დაბეჭდეთ ეს სამივე ცვლადი


number1 =float(input("enter your number1: "))
number2 =int(input("enter your number2: "))
number3 =int(input("enter your number3: "))
print(number1 , number2 , number3)


'''საკლასო დავალება: შექმენით BMI კალკულატორი.
მომხმარებელს უნდა შეეკითხოთ წონა და სიმაღლე, შეინახეთ ათწილადის სახით.
შემდეგ შექმენით bmi ცვლადი, რომელიც ტოლია წონა / სიმაღლე ** 2. 
საბოლოოდ დაბეჭდეთთ ამ ცვლადის მნიშვნელობა
გააკეთეთ 5 მაგალითი თითო შედარების ოპერატორზე (>, <, >=, <=, ==, !=.)'''

weight = float(input("enter your weight: "))
height = float(input("enter your height: "))

bmi = weight / (height ** 2)

print(bmi)

num1=1 < 5
num2=4 < 7
num3=10 < 3
num4=328 > 863
num5=85 > 27
num6=456 > 457
num7=326 >= 478
num8=2854 >= 2455
num9=777 >= 777 
num10=2095 <= 8534
num11=5278 <= 1674
num12=1490 <= 1490
num13=174 != 427
num14=55 != 55
num15=869 != 479
num16=462 == 437
num17=92358 == 824
num18=4238 == 4238
