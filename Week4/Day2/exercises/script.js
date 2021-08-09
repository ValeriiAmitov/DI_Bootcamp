
//Exercise 1
function infoAboutMe() {
    console.log("My name is Valerii, I'm 30 years old and I'm married");
}
infoAboutMe();

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
    console.log("Your name is "+ personName + ", you are " + personAge+ " years old, your favorite color is "+ personFavoriteColor+ " and your hobbies are: ");
    for (hobbie in personHobbies) {
        console.log(personHobbies[hobbie]);
    }
}

infoAboutPerson("David", 45, "blue", ["Basketball", "Dancing"])
infoAboutPerson("Josh", 12, "yellow", ["Guitar playing", "Football", "Netflix"])


//Exercise 2
function checkDriverAge(age) {
    if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off");
    }
    else if (age > 18) {
        alert("You are old enough to drive, Powering On. Enjoy the ride!");
    }
    else if (age === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
}

checkDriverAge(18);

//Exercise 3
function checkNumber() {
    for (i=0; i<101; i++) {
        if (i%2 ===0) {
            console.log("The number " + i+ " is even");
        }
        else {
            console.log("The number " + i+ " is odd");
        }
    }
}
checkNumber();

//Exercise 4
function isDivisible(divisor) {
    let sum=0;
    for (i=0; i<501; i++) {
        if (i%divisor === 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log("sum: "+sum);
}
isDivisible(23);

//Exercise 5
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(){
    let item = prompt("Choose the item you like");
    if (item in amazonBasket) 
        alert("The item is in the basket");    
    else 
        alert("The item is not available");    
}

checkBasket();

//Exercise 6
function changeEnough([Quarters, Dimes, Nickels, Pennies], Price) {
    let sum = (Quarters*0.25) + (Dimes*0.1) + (Nickels*0.05) + (Pennies*0.01);
    if (sum >= Price) {
        console.log("true");
    }
    else {
        console.log("false");
    }
}

changeEnough([2, 100, 0, 0], 14.11);
changeEnough([0, 0, 20, 5], 0.75);

//Exercise 7
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];
function myBill() {
    let sum=0;
    for (let i=0; i<shoppingList.length; i++){
      if (shoppingList[i] in stock && stock[shoppingList[i]] > 0){ // Checking if item is in stock        
        sum += prices[shoppingList[i]];     
       }
}
console.log(sum); //Sum price
}

myBill();

//Exercise 8
function calcul() {
    let bill = prompt("What the bill was there?");
    let tip;
    if (bill < 50) {
        tip = parseInt((bill * 0.2));
    }
    else if (bill <= 200) {
        tip = parseInt((bill * 0.15));       
    }
    else if (bill > 200) {
        tip = parseInt((bill * 0.1));        
    }    
    console.log("The tip should be: $" + tip);
    console.log("The final bill is: $" + (+bill + tip));
}

calcul();

//Exercise 9
function hotelCost() {
    let nights = prompt("How many nights will you stay in the hotel?");
    if (!nights || isNaN(nights)) {
        hotelCost();
    }
    else {
        return (+nights * 140);       
    }
    
}

function planetRideCost() {
    let destination = prompt("Where are you going?");
     if (destination === "London") {
        return 183;    
    }
    else if (destination === "Paris") {
        return 220;
    }
    else if (destination) {
        return 300;
    }
    else if (!destination) {
        planetRideCost();
    }
    }

  function rentalCarCost() {
      let days = prompt("How many days would you renting the car?");
      if (!days || isNaN(days)) {
          rentalCarCost();
      }
      let totalCost = (+days * 40);
      if (days >= 10) {
          totalCost = (totalCost - (totalCost*0.05));
      }
      return totalCost; 
      }
    
function totalVacationCost() {
    console.log(parseInt(hotelCost() + planetRideCost() + rentalCarCost()));
}

totalVacationCost();