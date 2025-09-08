# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ სახელი და შეინახეთ name ცვლადში.
# შემდეგ შემოატანინეთ არჩევანი (რომელიც იქნება "u" ან "l") და შეინახეთ ეს ინფორმაცია choice ცვლადში.
# თუ choice ტოლია "u"-სი, მაშინ მომხმარებლის სახელი გამოიტანეთ uppercase-ში.
# თუ choice ტოლია "l"-ის, მაშინ მომხმარებლის სახელი გამოიტანეთ lowercase-ში.
# სხვა შემთხვევაში, დაუბეჭდეთ wrong information.
name = input("enter your name: ")

choice = input("enter your choice ('u' or 'l'): ")

if choice == "u":
    print(name.upper())

elif choice == "l":
    print(name.lower())

else:
    print("wrong information")




# შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.
# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.
# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1
def manual_find(main_string, str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i + len(str_to_find)] == str_to_find:
            return i
    return -1

main_string = input("enter main str: ")
str_to_find = input("enter to_find str: ")
print(manual_find (main_string, str_to_find))




# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.
# შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_count ცვლადში.
# დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში
# მომხმარებლისგან მთავარი სტრინგის შეყვანა
main_str = input("Enter the main string: ")

str_to_count = input("Enter the string to count: ")

count = main_str.count(str_to_count)

print(f"'{str_to_count}' სტრინგი {count} ჯერ გვხვდება '{main_str}' სტრინგში.")




# საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_swapcase
def manual_swapcase(input_string):
    result = ""
    for char in input_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

user_input = input("Enter a string: ")
print(manual_swapcase(user_input))

