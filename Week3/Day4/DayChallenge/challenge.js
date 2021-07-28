var sentence = ("The chicken is not that bad, I like it");
var wordNot = sentence.substring(15, 18);
var wordBad = sentence.substring(24, 27);
let str = sentence.indexOf(wordNot);
if(str > -1){
    sentence = ("The chicken is good, I like it");
    console.log(sentence);
   
} else {
    console.log(sentnce);
}