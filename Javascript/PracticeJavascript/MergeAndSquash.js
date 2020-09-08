const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '11',
    '44',
    '69',
    '46',
    '63',
    '83',
    '13',
    '62',
    '14',
    '31',
    '68',
    '87'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;
 
let N = Number(gets())
let NumberAr = []
let mergedAr = []
let squashedAr = []

for(i = 0; i < N; i++){
    let number = gets()
    NumberAr.push(number)
}

for(let i = 0; i < NumberAr.length - 1; i++){
    let firstDig = NumberAr[i][1] 
    let secondDig = NumberAr[i + 1][0]
    mergedAr.push(firstDig + '' + secondDig)
}

for(let i = 0; i < NumberAr.length - 1; i++){
    let firstDig = Number(NumberAr[i][0])
    let secondDig = Number(NumberAr[i][1]) + Number(NumberAr[i+1][0])

    if(secondDig >= 10){
        secondDig = secondDig - 10
    }
    let thirdDig = Number(NumberAr[i+1][1])
    squashedAr.push(firstDig + '' + secondDig + '' + thirdDig)
}

for(let i = 0; i < mergedAr.length; i++){
    mergedAr[i] === mergedAr[i].split(' ').map(Number)
    squashedAr[i] === squashedAr[i].split(' ').map(Number)
}

print(...mergedAr)
print(...squashedAr)