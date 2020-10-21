const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '8',
    '7',
    '3',
    '2',
    '3',
    '5',
    '6',
    '2',
    '4'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = +gets()
let ar = []
let counter = 0
let maxcounter = 0
for(i = 0 ; i < N; i++){
    let numbers = +gets()
    ar.push(numbers)
}

for(x = 0; x < ar.length; x++){
    if(ar[x] < ar[x+1]){
        counter++
    }
    else{
        if(maxcounter < counter){
            maxcounter = counter
        }
        counter = 0
    }
}
print(maxcounter+1)
