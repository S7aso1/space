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
  '7'
];

const gets = this.gets || getGets(test);
const print = this.print || console.log;

let N = Number(gets())

for(let i = 0; i < N; i++){
    product = i * 5
    print(product)
}
