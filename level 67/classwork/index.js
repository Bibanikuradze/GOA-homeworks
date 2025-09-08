<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ece595cb226c55c0285bc5cb057ff43306b8a264
const student = {
    name: "ბიბა",
    surname: "ნიკურაძე",
    academy: "GOA",
    city: "თბილისი",
    role: "მოსწავლე",
    favColor: "frozen green",
    
    printFullName: function() {
        console.log(this.name + " " + this.surname);
    },

    printFavColor: function() {
<<<<<<< HEAD
=======
// შექმენით ობიექტი, სადაც გექნებათ შემდეგი გასაღებები: name, surname, academy, city, role, favColor - აქ შეინახავთ მარტივ მონაცემებს (string, number, boolean). კიდევ გექნებათ ობიექტის მეთოდი, რომელიც გამოიტანს კონსოლში ობიექტის სახელს და გვარს ერთად. დაამატეთ კიდევ ერთი მეთოდი, რომელიც გამოიტანს ობიექტის favColor გასაღების მნიშვნელობას.

// მეთოდებზე მუშაობისას გამოიყენეთ this keyword.

// 1. კონსოლში დაბეჭდეთ მთლიანი ობიექტი.
// 2. კონსოლში დაბეჭდეთ ნებისმიერი კუთვნილება ობიექტის.
// 3. გამოიძახეთ ობიექტის რომელიმე მეთოდი.
// 4. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა და შემდეგ კონსოლში დაბეჭდეთ ეს მნიშვნელობა

let object1 = {
    name: "Nini",
    surname: "Pheradze",
    academy: "GOA",
    city: "Zestafoni",
    role: "Student",
    favColor: "White",
    logFullname(){
        console.log(this.name + " " + this.surname);
    },
    logColor(){
>>>>>>> 7ac26f8 (commit)
=======
>>>>>>> ece595cb226c55c0285bc5cb057ff43306b8a264
        console.log(this.favColor);
    }
};

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ece595cb226c55c0285bc5cb057ff43306b8a264
console.log(student);

console.log(student.city);

student.printFullName();

student.favColor = "frozen green";
console.log(student.favColor);









function userOperations() {
  let answer1 = confirm("გსურს პროგრამირების სწავლა?");
  let answer2 = confirm("გსურს GOA-ში სწავლა?");

  console.log("AND ოპერაცია (answer1 && answer2):", answer1 && answer2);
  console.log("OR ოპერაცია (answer1 || answer2):", answer1 || answer2);
}

<<<<<<< HEAD
window.onload = userOperations;
=======
// 1.კონსოლში დაბეჭდეთ მთლიანი ობიექტი.
console.log(object1);

// 2. კონსოლში დაბეჭდეთ ნებისმიერი კუთვნილება ობიექტის.
console.log(object1.surname);

// 3. გამოიძახეთ ობიექტის რომელიმე მეთოდი.
object1.logFullname();

// 4. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა და შემდეგ კონსოლში დაბეჭდეთ ეს მნიშვნელობა
object1.favColor = "Green";
console.log(object1.favColor)



// შექმენით ფუნქცია სახელად userOperations. ამ ფუნქციაში აიღეთ ორი ცვლადი და მათში შეინახეთ confirm box-ის შედეგები.

// შემდეგ დაბეჭდეთ ამ ორ ცვლადს შორის and და or ლოგიკური ოპერაციების შედეგები.

// ეს ფუნქცია გამოიძახეთ მაშინ, როდესაც ვებსაიტი ჩაიტვირთება

function userOperations(){
    let bool1 = confirm("Do you live in Georgia?");
    let bool2 = confirm("Do you study in GOA?");

    console.log(bool1 || bool2);
    console.log(bool1 && bool2);
}

userOperations();
>>>>>>> 7ac26f8 (commit)
=======
window.onload = userOperations;
>>>>>>> ece595cb226c55c0285bc5cb057ff43306b8a264
