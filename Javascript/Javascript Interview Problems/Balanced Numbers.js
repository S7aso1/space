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
  '123',
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

const isBalanced = (n) => Number(n[0]) + Number(n[2]) === Number(n[1]);

let sum = 0;

let currentNum = gets();

while (isBalanced(currentNum)) {
  sum += Number(currentNum);
  currentNum = gets();
}

print(sum);