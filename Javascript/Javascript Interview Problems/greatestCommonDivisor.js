const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '5 15',
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let [A, B] = gets().split(' ').map(Number)
let max = Math.max(A, B);
let min = Math.min(A, B);

let greatestCommonDevisor = function(a, b){
    let remainder = a % b
    if(remainder === 0){
        return b
    }
    a = b 
    b = remainder
    return greatestCommonDevisor(a, b)
}


print(greatestCommonDevisor(max,min))