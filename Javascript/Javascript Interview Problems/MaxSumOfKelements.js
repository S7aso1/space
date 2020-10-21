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
    '3',
    '3',
    '2',
    '3',
    '-2',
    '5',
    '4',
    '2',
    '7'	
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = Number(gets())
let K = Number(gets())
let arr = []
let maxArr = []
let sum = 0

for(i = 0; i < N; i++){
    arr.push(Number(gets()))
}

arr.sort(function(a, b){return a-b});

for(x = 1; x <= K; x++){
    maxArr.push(arr[arr.length - x])
}

for(y = 0; y < maxArr.length; y++){
    sum = sum + maxArr[y]
}
print(sum)