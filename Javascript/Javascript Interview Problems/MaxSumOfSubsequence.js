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
    '3',
    '-6',
    '-1',
    '2',
    '-1',
    '6',
    '4',
    '-8',
    '8'
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;
//////////////////////////////////////////////
let N = Number(gets())
let numHolder = []
let num = 0
let sum = 0
let sumHolder = []

if(1 <= N && N <= 1024){
    for(i = 0 ; i < N ; i++){
        num = gets()
        numHolder.push(Number(num))
    }

    for(i = 0 ; i < numHolder.length; i++){
        sum += numHolder[i]
        for(x = i + 1; x < numHolder.length; x++){
            sum += numHolder[x]
            sumHolder.push(sum)
        }
        sum = 0
    }


    sumHolder.sort(function(a, b){
        return b - a 
    })
    print(sumHolder[0])
}