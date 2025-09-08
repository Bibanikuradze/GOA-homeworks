'''
int
42
-10
1000
0
-5
500
2010
123456789
-999
7

str

"Hello"
"Python"
"12345"
"True"
"My name is Biba"
"abc"
"2024"
"apple"
"It's a nice day!"
"GOA"

float 

3.14
-0.001
2.71828
-42.5
0.0
100.0
-9999.99
56.789
1.0
3.14159265358979
'''


# თქვენი სიტყვებით ახსენით რა დროს გვჭირდება მონაცემთა ტიპის კონვერტაცია:
'''ზოგჯერ გვჭირდება, რომ გარკვეული მონაცემები კონკრეტულ ტიპში არსებობდეს. მაგალითად,
თუ გვაქვს str  "123" მაგრამ გვინდა რომ შევიტანოთ რიცხვი,
მას უნდა გადავაქციოთ int ტიპში, რათა შევძლოთ მათემატიკური ოპერატციების ჩატარება'''


#შემდეგ 6 შედარების ოპერატორზე: >, <, >=, <=, !=, == ჩამოწერეთ 10-10 მაგალითი, გამოიყენეთ ცვლადები
num1=1 < 5
num2=4 < 7
num3=10 < 3
num4=328 > 364
num5=85 > 27
num6=456 > 457
num7=326 >= 478
num8=2854 >= 2455
num9=777 >= 777 
num10=2095 <= 2555
num11=1673 <= 1674
num12=1490 <= 1490
num13=174 != 427
num14=55 != 55
num15=845 != 479
num16=462 == 437
num17=92358 == 92358
num18=40723 == 4822


# მომხმარებელს შემოატანინეთ ასაკი და დაუბეჭდეთ 10 წელში რამდენი წლის იქნება
age = int(input ("enter your age: "))
new_age = age + 10
print(new_age)


# სამ ადამიანს შემოატანინეთ ასაკები და გამოითვალეთ ამ ასაკების საშუალო არითმეტიკული (ასაკების ჯამი / ადამიანების რაოდენობა)
age1 = int(input("enter your age: "))
age2 = int(input("enter your age: "))
age3 = int(input("enter your age: "))
total_age = age1 + age2 + age3
average_age = total_age / 3
print(int(average_age))


# მომხმარებელს შემოატანინეთ 2 რიცხვი და დაბეჭდეთ ამ რიცხვების: ჯამი, სხვაობა, ნამრავლი, განაყოფი, პირველი რიცხვი ხარისხად მეორეზე, მეორე რიცხვი ხარისხად პირველზე
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num2 / num1 if num1 != 0 else "განუსაზღვრელი")    


# მომხმარებელს შემოატანინეთ 3 რიცხვი და დაბეჭდეთ ამ რიცხვების: ჯამი, სხვაობა, ნამრავლი, განაყოფი
number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 ** number2)
print(number2 / number1 if number1 != 0 else "განუსაზღვრელი")  