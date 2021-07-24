let a = 2 + 2;

switch (a) {
  case 4:
    alert('Right!'); //That's one, because of correct value of (a) is 4. Even if we have a structure - when the answer is right our code switch the correct case. If it false a block will continue.
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}