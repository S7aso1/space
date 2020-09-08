const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    'lony',
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let ar = gets().split('')


for(i = 0; i < ar.length; i++){
    let msgCopy = ''
    let msg = msgCopy + ar[i] + msgCopy
    msgCopy == msg
    print(msg)
}
