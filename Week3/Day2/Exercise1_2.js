let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]); 
//We have the array with few levels of elements. First level includes two elements: 
//"Banana" (0) and ["Apples", ["Oranges"], "Blueberries"] (1),
//As far as we need to get "Oranges" we choose to select (1).
//Inside element (1) we have next level which includes three elements and we need to choose ["Oranges"] (1)
//And the third level includes only one element "Oranges" (0)