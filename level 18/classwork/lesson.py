# საკლასო დავალება 1: 0-დან 20-მდე დაბეჭდეთ ლუწი რიცხვები. არ გამოიყენოთ if - პირობითი განცხადება.

odd_0_20 = list(range(0 , 20 , 2))
print(odd_0_20)


# საკლასო დავალება 2: 0-დან 20-მდე დაბეჭდეთ კენტი რიცხვები. არ გამოიყენოთ if - პირობითი განცხადება.

even_0_20 = list(range(1 , 20 , 2))
print(even_0_20)


# საკლასო დავალება 3: 10-დან 30-ის ჩათვლით დაბეჭდეთ ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი,
# მაგ: 10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლით

num1 = int(input("Enter number: "))
if num1 %2 == 0:
    print(str(num1), "is even")
else:
    print(str(num1), "is odd")


# საკლასო დავალება: მომხმარებელს შემოატანინეთ 2 რიცხვი, num1, num2.
# თუ პირველი მეტია მეორეზე, შექმენით დიაპაზონი მეორე რიცხვიდან პირველი რიცხვის ჩათვლით და დაბეჭდეთ მხოლოდ ლუწი.
# ხოლო თუ მეორე რიცხვი მეტია პირველზე, შექმენით დიაპაზონი პირველიდან მეორეს ჩათვლით და დაბეჭდეთ მხოლოდ კენტი რიცხვები.
# საბოლოოდ დაბეჭდეთ ყველა ამ დაბეჭდილი რიცხვის ჯამი.

num1, num2 = int(input("Enter your number: ")), int(input("Enter your number: "))

if num1 > num2:
    range1 = range(num2, num1 + 1)
    sum1 = 0

    # print only even numbers
    for i in range1:
        if i%2 == 0:
            print(i)
            sum1 += i
    
    print("Sum of all even numbers are:", str(sum1))
else:
    range2 = range(num1, num2 + 1)
    sum2 = 0

    # print only odd numbers
    for i in range2:
        if i%2 != 0:
            print(i)
            sum2 += i
    
    
    print("Sum of all even numbers are:", str(sum2))