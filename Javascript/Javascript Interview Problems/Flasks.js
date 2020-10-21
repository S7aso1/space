const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '10 34'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let [numerOfFlasks, totalLiquid] = gets().split(' ').map(Number)
let allFlasks = []
let allSizes = [0]
let oddFlasks = []
let oddSizes = []

for(i = 1 ; i <= numerOfFlasks; i++){
    allFlasks.push(i) 
}

let sum = 0
for(i = 0 ; i < allFlasks.length; i++){
    sum = allFlasks[i]+allSizes[i]
    allSizes.push(sum) 
}

let index = 0
for(i = 0 ; i < allFlasks.length; i++){
    if(allFlasks[i] % 2 !== 0){
        oddFlasks.push(allFlasks[i]) 
        index = allFlasks.indexOf(allFlasks[i])
        oddSizes.push(allSizes[index]) 
    }
}

for(i = 0; i < oddSizes.length; i++){

    let flaskSize = oddSizes[i]
 
    if(flaskSize >= totalLiquid){
        print(oddFlasks[i])
        break;
    } 
    else if(flaskSize < totalLiquid) {
        break;
    }
}