function handleSubmit(event) {
  event.preventDefault();

  const input = document.getElementById('username');
  const value = input.value;

  console.log("შეყვანილი მნიშვნელობა:", value);
}




function concStrings() {
  let firstString = prompt("შეიყვანე პირველი სტრინგი:");
  let secondString = prompt("შეიყვანე მეორე სტრინგი:");
  
  let result = firstString + secondString;

  alert("შედეგი: " + result);
}
