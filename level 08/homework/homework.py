# თქვენი სიტყვებით ახსენით რა არის input და output, რამდენი ნაკადი გვაქვს და თითოეულისთვის რა ბრძანებას ვიყენებთ პითონში
# num1=input("enter your number: ")

'''
input- არის ინფორმაცია რასაც კომპიუტერს ვაწვდით  / მაგ: input ფუნქცია
ხოლო 
output- არის ინცორმაცია რასაც კომპიუტერი გვაწვდის / მაგ: PRINT
''' 

num1 = 10
num2 = 3.14
hello = "Hello World!"

print(type(num1)) 
print(type(num2)) 
print(type(hello))

# მომხმარებელს შემოატანინეთ სახელი და გვარი, შეინახეთ ისინი ცვლადებში. შემდეგ დაუბეჭდეთ: "გამარჯობა {სახელი აქ} {გვარი აქ}."

name=input("enter your name: ")
surname=input("enter your surname: ")
print(f"hello {name} , {surname}")

#შექმენით 5 ცვლადი და მათში შეინახეთ რიცხვები. შემდეგი 6 ოპერატორის გამოყენებით: +, -, *, /, **, %  ჩამოწერეთ მათ შორის მათემატიკური ოპერაციები. ჩამოწერეთ ასეთი 10 მაგალითი.

num1=1
num2=10
num3=100
num4=1000
num5=10000

print(num1+num2)
print(num4-num3)
print(num4*num1)
print(num5/num3)
print(num2**num3)
print(num4%num2)
