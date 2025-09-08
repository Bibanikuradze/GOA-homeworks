''' საკლასო დავალება: True, False ბულეანებზე ჩამოწერეთ 4 კომბინაცია.
ეს გააკეთეთ ან ოპერატორზეც და და ოპერატორზეც.
თითეოული კომბინაციის შედეგი უნდა დაიბეჭდოს და მარჯვნივ მიუწერეთ კომენტარის სახით შედეგი რაც არის'''

print("true or true")       #true
print("false or true")      #true
print("true or false")      #true
print("false or false")     #false

print("false and false")     #true
print("true and false")      #false
print("false and true")      #false
print("true and true")       #false



''' მომხმარებელს ინფუთით შემოატანინეთ რიცხვი და გადააქციეთ ის მთელი რიცხვად, შეინახეთ ცვლადში. ასევე იგივე გააკეთეთ მეორე რიცხვზე.
შემდეგ დაბეჭდეთ: პირველი რიცხვი მეტია 30-ზე და მეორე ნაკლებია 40-ზე'''

num1=int(input("enter num1"))
num2=int(input("enter num2"))
print(num1 > 30 and num2 < 40)