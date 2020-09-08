const getGets = (arr) => {
    let index = 0;

    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
// this is the test
const test = [
    '4',
    '2'
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let n = gets()
let k = gets()
let NminusK = n - k 


function factorial(n){
    let i, result = BigInt(1)
    
    for(i = BigInt(2); i <= n; i++){
        result *= i;
    }
    return result
}
print(factorial(n) / (factorial(k) * factorial(NminusK)))