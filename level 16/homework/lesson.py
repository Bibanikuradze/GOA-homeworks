# გააკეთეთ ნახაზი while ციკლის შესახებ და დეტალურად ახსენით თუ ის როგორ მუშაობს
# მაგალითად: 
'''
while user_num != my_num:
    user_num = int(input("Enter number: "))
    counter += 1

while ციკლის დროს არ არის იტერაციის რაოდენობა ყოველთვის სწორი
სანამ while ციკლის პირობა სწორია მანამდე გაეშვება კოდის ბლოკი,
ხოლო როცა დამთავრდება სწორი კოდი მაშინ შეწყდება კოდის წერა.
'''

# თქვენი სიტყვებით ახსენით განსხვავება while და for ციკლებს შორის
'''
while (loop) ციკლის დროს ყოველთვის იტერაციის რაოდენიბა სწორი არ არის,
ხოლო for (loop) ციკლის დროს ცნობილია იტერაციის რაოდენობა
'''

# დაბეჭდეთ "GOA BEST!!!" 50-ჯერ, ორივე ციკლით შეასრულეთ ეს დავალება
count = 0
while count < 50: 
    print("goa best")
    count += 1 

for i in range(50): 
    print("goa best")
    
# Write a program that uses a while loop to count from 1 to 10 and prints each number.
count = 1
while count < 10 + 1: 
    print(count)
    count += 1

# Use a while loop to print all even numbers between 1 and 20.
count = 1
while count < 20 + 1: 
    print(count)
    count += 2

# Create a countdown from 10 to 1 using a while loop, and print "Blast off!" when the countdown finishes.
count_down = 10
while count_down > 0: 
    print(count_down)
    count_down -= 1
print("blast off")
    
# Prompt the user to enter a password. Keep asking until they enter the correct password.
# prompt ნიშნავს რომ შემოატანინოთ
# Create a program that keeps asking for a username and password until both are correct.
correct_username = "biba"
correct_password = "nikuradze"
while True :
    user_input = input("enter your username: ")
    user_password = input("enter your password: ")
    if user_input != correct_username or user_password != correct_password:
        print("incorrect username or password. please try again.")
    else: 
        print("Login successful!")
        break