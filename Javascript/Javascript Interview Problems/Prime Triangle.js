const getGets = (arr) => {
  let index = 0;

  return () => {
    const toReturn = arr[index];
    index += 1;
    return toReturn;
  };
};
// this is the test
const test = ['10'];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

const isPrime = (num) => {
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
};

let n = +gets();

let rows = 0;

for (let i = 1; i <= n; i++) {
  if (isPrime(i)) {
    rows++;
  }
}

const func = (n) => {
  let line = '';
  for (let i = 1; i <= n; i++) {
    line += isPrime(i) ? '1' : '0';
  }

  print(line);
}

for (let i = 1; i <= n; i++) {
  if (isPrime(i)) {
    func(i);
  }
}