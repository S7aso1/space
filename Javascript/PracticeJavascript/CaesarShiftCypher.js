let input = 3;
let basicStr = 'YHQL'
let arrOfStr = basicStr.toLowerCase().split('')
let charCodes = []
let resultStr = []
let absoluteVal = 0

for(i = 0 ; i < arrOfStr.length ; i++){
    charCodes.push(arrOfStr[i].charCodeAt() + 3)


        if(charCodes[i] > 122){
            absoluteVal = Math.abs(122 - charCodes[i]) + 96
            resultStr.push(String.fromCharCode(absoluteVal))
        }
        else{
            resultStr.push(String.fromCharCode(charCodes[i]))
        }
        
}
console.log(resultStr.join(''))