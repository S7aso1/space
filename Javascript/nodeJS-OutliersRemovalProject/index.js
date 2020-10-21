/**
 * Used library:
 * https://www.npmjs.com/package/csv-parser
 * 
 * File reading:
 * https://nodejs.org/api/fs.html
 * https://nodejs.org/api/stream.html
 */
const fs = require('fs');
const csv = require('csv-parser');

let rows = [],
    pressures = [],
    temperatures = [],
    humidities = []

function main() {
    const fileName = "test.csv"
    processCSV(fileName)
}

function processCSV(fileName) {
    fs.createReadStream(fileName)
        .on('error', (err) => {
            console.log(err)
            // handle error
        })

        .pipe(
          csv({
            separator: ';'
        })
        )
        .on('data', (row) => {
            rows.push(row)
        })


        .on('end', () => {
            processRows()
            console.log('rows are processed')

           
            console.log(`filering pressures`)
            pressures = removeOutliers(pressures)
            
            console.log(`filering temps`) 
            temperatures = removeOutliers(temperatures)

            console.log(`filering humidities`) 
            humidities = removeOutliers(humidities)

             writeDataToCsv(humidities,'humidities')
             writeDataToCsv(temperatures,'temperatures')
             writeDataToCsv(pressures,'pressures')
            

        })
}

function processRows() {
    rows.map(row => {
        pressures.push([row['pressure']])
        temperatures.push(row['temperature'])
        humidities.push(row['humidity']);
  
    })

}


function findMid(min, max) {
    var noOfItems = max - min;
    if (noOfItems % 2 != 0) {
        var mid = Math.floor((min + max) / 2)
        return [mid]
    } else {
        var mid = Math.floor((min + max) / 2)
        var midOther = mid - 1;
        return [mid, midOther]
    }
}

function removeOutliers(data) {

    var sortedData = JSON.parse(JSON.stringify(data))
    sortedData.sort((a, b) => {
        return a - b
    })

    //find the mid
    var bigMid = sortedData.length / 2 //126
    var q1Mid = findMid(0, bigMid) //0,126

    if (q1Mid.length == 2) {
        var num1 = q1Mid[0]
        var num2 = q1Mid[1]
        var q1 = (Number(sortedData[num1]) + Number(sortedData[num2])) / 2
    } else { 
        var num1 = q1Mid[0]
        var q1 = Number(sortedData[num1])
    }

    var q3Mid = findMid(bigMid,sortedData.length)




    if (q3Mid.length == 2) {
        var num1 = q3Mid[0]
        var num2 = q3Mid[1]
        var q3 = (Number(sortedData[num1]) + Number(sortedData[num2])) / 2
    } else { //only got 1 mid number
        var num1 = q3Mid[0]
        var q3 = Number(sortedData[num1])
    }


    var data = data.filter((data) => {
        return data > q1;
    }) //data = good data [], bad data removed

    var data = data.filter((data) => {
        return data < q3;
    }) //data = good data [], bad data removed


    return data;


}

function writeDataToCsv(data,name) {
    data = data.join('\r\n')
    data = name + '\r\n' + data
    fs.writeFile(name +'.csv',data, 
    (err)=> { console.error(err) },
    () => { console.log(name + ' written') })
  
  }

main();



