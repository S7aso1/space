let n = 34
var count = 0;
let resultArr = []

    while(n !== 1) {
        if(n % 2 === 0) {
            n /= 2;
        } else {
            n = (3 * n) + 1;
        }
        count++;
        resultArr.push(n)
}


console.log('Steps to reach 1: ' + count)
console.log(resultArr.toString());

