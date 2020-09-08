const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '3',
    '5 0 1',
    '7 4 -3'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = Number(gets())
let firstPoly = gets().split(' ').map(Number)
let secondPoly = gets().split(' ').map(Number)
let result = []

for(i = 0; i < N; i++){
    result.push(firstPoly[i] + secondPoly[i])
}
print(result.join(' '))