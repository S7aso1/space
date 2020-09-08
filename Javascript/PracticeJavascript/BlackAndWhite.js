const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '2',
    '2'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = Number(gets())
let M = Number(gets())
let NxM = N * M
let squares = []
let counter = 1

for(i = 0; i < NxM; i++){
    squares.push('w')
}
console.log(squares)

for(i = 0 ; i < squares.length ; i++){
    squares.splice(i, 1)
    squares.splice(i, 0, 'b')
    if(i >= 1){
    squares.splice(i - 1, 1)
    squares.splice(i - 1, 0, 'w')
    }
    counter++
    console.log(squares)
}
console.log(counter)

for(i = squares.length; i > 0; i--){
    
}