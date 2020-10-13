const request = require('request')

var getWeather = (lat, lng, callback) => {
    request ({
        url: `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=PASTE-THE-API-KEY-HERE`,
        json: true
    }, (error, response, body) => {
        if(!error && response.statusCode == 200){
            callback(undefined, {
                temperature: body.main.temp,
                apparentTemperature: body.main.feels_like
            })
            
        }else{
            callback('Unable to fetch weather')
        }
    })
}


module.exports.getWeather = getWeather