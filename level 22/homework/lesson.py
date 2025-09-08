# 2) თქვენი სიტყვებით ახსენით რა არის slicing, გააკეთეთ ნახაზი ამ საკითხზე
# Slicing არის მეთოდი, რომელიც გამოიყენება მონაცემთა სტრუქტურებში როგორიცაა list 
# მაგალითად:listn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# listn[2:7:2]

# 3) შექმენით სია, რომელშიც იქნება 10 ელემენტი. გადაუარეთ სიას ციკლით და დაბეჭდეთ მისი ყველა ელემენტი
listn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in listn:
    print(i)

# 4) შექმენით სია, რომელშიც იქნება 10 ელემენტი. მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი, num1 და num2. 
# თუ num1 მეტია num2-ზე, slicing მოახდინეთ სიაზე num1 ინდექსიდან num2 ინდექსამდე და დაბეჭდეთ ახალი სია.
# თუ num2 მეტია num1-ზე, slicing მოახდინეთ სიაზე num2 ინდექსიდან num1 ინდექსამდე და დაბეჭდეთ ახალი სია.
# თუ ეს ორი რიცხვი ტოლია, დაბეჭდეთ ცარიელი სია.
listn1 =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
if num1 > num2:
    print(listn1[num1:num2])
elif num2 > num1:
    print(listn1[num2:num1])
else:   
    print([])

# 5) Given a list of numbers, print the first, third, and last elements using indexing.
listn2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listn2[0])
print(listn2[2])
print(listn2[-1])

# 6) Given a list of strings, print the list in reverse order using slicing.
# Reverse order - შებრუნებული სია
listn3 = ["biba", "nika" ,"luka" ,"gio"]
print(listn3[::-1])

# 7) Given a list of words, print every second element starting from the first element. (ერთი ელემენტის გამოტოვებით)
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(words[::2])

# 8) Given a list of numbers, replace the fourth element with the number 100 and print the modified list.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[3] = 100
print(numbers)