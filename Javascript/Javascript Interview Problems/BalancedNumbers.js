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
    '132',
    '123'

  ];
  

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let BalancedNumberArray = []

for(i = 0; i < test.length; i++){ /// test.length is not valid
    let number = gets()
    if(Number(number[0]) + Number(number[2]) === Number(number[1])){
        BalancedNumberArray.push(Number(number))
    }
}
let sum = 0
for(i = 0; i < BalancedNumberArray.length; i++){
    sum += BalancedNumberArray[i]
}

print(sum)
