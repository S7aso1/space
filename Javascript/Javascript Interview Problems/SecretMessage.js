const getGets = (arr) => {
    let index = 0;
    return () => {
        const toReturn = arr[index];
        index += 1;
        return toReturn;
    };
};
const test = [
    'o2hs123o6G0ol090le42H',
];
const gets = this.gets || getGets(test);
const print = this.print || console.log;

let message = gets().split('')
message.reverse()
let filtereddmessage = []

for(i = 0; i < message.length; i++){
    if(isNaN(message[i])){
        filtereddmessage.push(message[i])
    }
}
print(filtereddmessage.join(''))