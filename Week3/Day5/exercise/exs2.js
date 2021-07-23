let names = ["john", "sarah", 23, "Rudolf", 34];
for (let i = 0; i < names.length; i++) {
  if (typeof names[i] === "string") {
    if (names[i][0] !== names[i][0].toUpperCase()) {
      names[i] = names[i][0].toUpperCase() + names[i].slice(1);
      console.log(names[i]);
    }
  }
}
let names = ["john", "sarah", 23, "Rudolf", 34];
for (let i = 0; i < names.length; i++) {
  if (typeof names[i] === "string") {
    continue;
  }
  if (names[i][0] !== names[i][0].toUpperCase()) {
    names[i] = names[i][0].toUpperCase() + names[i].slice(1);
    console.log(names[i]);
  }
}