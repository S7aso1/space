const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '100',
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let array = gets().split('').map(Number)
let sum = 0 
let one = 1
let power = 0
let indecies = []
let powersHolder = []

let sortedar = array.sort(function (a,b){
    return b - a 
})

let index = sortedar.indexOf(one)

while(index != -1){
    indecies.push(index)
    index = array.indexOf(one, index + 1);
}

for(i=0; i<indecies.length; i++){
    power = 2 ** indecies[i]
    powersHolder.push(power)
}

for(i=0; i<powersHolder.length; i++){
    sum += powersHolder[i]
}
console.log(sum)