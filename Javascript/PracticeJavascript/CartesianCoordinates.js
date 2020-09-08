const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    '0',
    '0'
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let x = Number(gets())
let y = Number(gets())

if(x > 0 && y > 0){
    print(1)
}
if(x < 0 && y > 0){
    print(2)    
}
if(x < 0 && y < 0){
    print(3)
}
if(x > 0 && y < 0){
    print(4)
}
if(x === 0 && y !== 0){
    print(5)
}
if(y === 0 && x !== 0){
    print(6)
}
if(y === 0 && x === 0){
    print(0)
}