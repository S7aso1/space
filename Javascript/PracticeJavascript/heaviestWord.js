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
    '5',
    'telerik',
    'alpha',
    'java',
    'Spring',
    'nodeJS'
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;


let amountLoops = Number(gets())
let weightArray = []
let inputArray = []
let weightOfLetter = 0
let weightSum = 0 


for(i = 0; i < amountLoops; i++){
    let inputData = gets()    
    inputArray.push(inputData)    
    let stringAr = inputData.toLowerCase().
    split('')

    for(j = 0; j < stringAr.length; j++){
        weightOfLetter = (stringAr[j].charCodeAt() - 96)
        weightSum += (weightOfLetter)
    }
    weightArray.push(weightSum)
    weightSum = 0
}
let highestWeight = Math.max(...weightArray)
let indexOfHighest = weightArray.indexOf(highestWeight)
print(inputArray[indexOfHighest] + ' ' + weightArray[indexOfHighest])
