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
    'anagram',
    '6',
    'gramana',
    'aaagrnm',
    'anagra',
    'margana',
    'abc',
    'xy'
]
 
const gets = this.gets || getGets(test);
const print = this.print || console.log;
 
let W = gets().split("").sort().join("") //Split into array; sort them out; Join them back in a string

let NumberOfWords = gets()
let matchedArr = []
 
for(let i = 0; i < NumberOfWords; i++){

    let WORDS = gets().split("").sort().join("") //Split into array; sort them out; Join them back in a string
    
    if (W == WORDS) { //Check if sorted words are the same 
    console.log('Yes')
    }
    else {
     console.log('No')
    }
}