const MOM = 2;
const DAD = 1.2;

function myAge(myAge) {
    let mumAge= myAge*MOM;
    let dadAge= mumAge*DAD;
    
    console.log("my mum\'s age is "+ mumAge +"my dad\'s age is " + dadAge);
}
myAge(30);