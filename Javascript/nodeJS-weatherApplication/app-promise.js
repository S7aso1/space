const yargs = require('yargs')
const axios = require('axios')

const argv = yargs.options({
    a: {
        demand: true,
        alias: 'address',
        describe: 'Address to fetch weather for',
        string: true
    }
})
    .help().alias('help', 'h').argv

var encodedAddress = encodeURIComponent(argv.address)
var geocodeUrl =  `https://maps.googleapis.com/maps/api/geocode/json?address=${encodedAddress},+CA&key=PASTE-THE-API-KEY-HERE`


axios.get(geocodeUrl).then((response) => {
    if(response.data.status === 'ZERO_RESULTS'){
        throw new Error('Unable to find the address')
    }
    var lat = response.data.results[0].geometry.location.lat
    var lng = response.data.results[0].geometry.location.lng
    var weatherUrl = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=PASTE-THE-API-KEY-HERE`
    console.log(response.data.results[0].formatted_address)
    return axios.get(weatherUrl)

}).then((response) => {
    var temperature = response.data.main.temp
    var apparentTemperature = response.data.main.feels_like
    console.log(`It's currently ${temperature}. It feels like ${apparentTemperature}.`)
    
}).catch((e) => {
    if(e.code === 'ENOTFOUND'){
        console.log('Unable to connect to api servers')
    }else {
        console.log(e.message)
    }
})