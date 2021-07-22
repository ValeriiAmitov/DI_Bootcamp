let names = ["john", "sarah", 23, "Rudolf", 34]
for (let name of names) {
    if(typeof(name) !== "string") {
        break;
    }
    console.log(name);
}
