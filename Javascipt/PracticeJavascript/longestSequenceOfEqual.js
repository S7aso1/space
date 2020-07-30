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
    '10',
    '2',
    '1',
    '1',
    '2',
    '3',
    '3',
    '2',
    '2',
    '2',
    '1'
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = Number(gets())
let arr = []

for (i  = 0; i < N; i++){
    arr.push(Number(gets()))
}

let counter = 1
let maxCounter = 1

for(i = 0; i < arr.length - 1; i++){
    if(arr[i] == arr[i+1]){
        counter++
        if(counter > maxCounter){
            maxCounter = counter
        }
    }else {
        counter = 1
    }
    arr[i] = arr[i+1]
}
print(maxCounter)
