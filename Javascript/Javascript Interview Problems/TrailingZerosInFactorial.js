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
    '100000',
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let num = Number(gets())
let result = []
let sum = 0

for(i = 0; i <= num; i++){
    num = Math.floor(num/5) 
    result.push(num)
}

for(i = 0 ; i < result.length; i++){
    sum += result[i]
}
print(sum)