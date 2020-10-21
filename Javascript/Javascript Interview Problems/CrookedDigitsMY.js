const getGets = (arr) => {
    let index = 0;
  
    return () => {
      const toReturn = arr[index];
      index += 1;
      return toReturn;
    };
  };
  // this is the test
  const test = ['-7231'];
  
  const gets = this.gets || getGets(test);
  const print = this.print || console.log;
  
let arr = gets().split('')

let nanCheck = function(n){
    if (isNaN(n)) {
        return false;
      }
  
      return true;
}

let filteredArr = arr.filter(nanCheck).map(Number)

//console.log(arr)
//console.log(filteredArr)

let sum = 0
for(i=0; i<filteredArr.length; i++){
    sum = sum + filteredArr[i]
}
//console.log(sum)

if(sum >= 9){
    sumSplit = sum.toString().split('').map(Number)
    console.log(sumSplit)
}

let newsum = 0
for(i=0; i<sumSplit.length; i++){
    newsum += sumSplit[i]

}
console.log(newsum)