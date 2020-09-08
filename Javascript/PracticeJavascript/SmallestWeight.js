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
    'acceptable funny slippery scribble nasty'
]

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let words = gets().split(' ')
let alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
let sum = 0
let sumHolder = []

for(let i = 0; i < words.length; i++){

    for(let x = 0; x < words[i].length; x++){
        let powerOfLetter = alphabet.indexOf(words[i][x]) + 1
        sum += powerOfLetter
        
    }
    sumHolder.push(sum)
    sum = 0
}

console.log((sumHolder))
let smallestWeight = Math.min(...(sumHolder))
let indexOfSmallestWeight = sumHolder.indexOf(Math.min(...(sumHolder)))

console.log(smallestWeight + ' ' + words[indexOfSmallestWeight])
