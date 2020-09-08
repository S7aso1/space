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
    '8',
    '3'
]

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let n1 = gets()
let n2 = gets()

function factorial(n){
    let i, result = BigInt(1)
    
    for(i = BigInt(2); i <= n; i++){
        result *= i;
    }
    return result
}
print(factorial(n1) / factorial(n2))