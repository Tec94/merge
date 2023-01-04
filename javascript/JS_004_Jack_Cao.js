function min(a, b) {
    if (Math.min(a) < Math.min(b)) {
        return Math.min(a);
    } else {return Math.min(b);}
}

console.log(min(0, 10));
console.log(min(0, -10));