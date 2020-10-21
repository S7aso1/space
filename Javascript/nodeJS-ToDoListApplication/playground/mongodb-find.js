//const MongoClient = require('mongodb').MongoClient
const {MongoClient, ObjectID} = require('mongodb') //destructuring

MongoClient.connect('mongodb://localhost:27017/TodoApp',(err, db) =>{
    if(err){
        return console.log('unable to connect to mongo db server')
    }
    console.log('connected to mongo db server')

    // db.collection('Todos').find({
    //     _id: new ObjectID('5f8d5689dae7692748428412')
    // }).toArray().then((docs) => {
    //     console.log('Todos')
    //     console.log(JSON.stringify(docs, undefined, 2))
    // }, (err) => {
    //     console.log('unable to fetch todos', err)
    // })

    // db.collection('Todos').find().count().then((count) => {
    //     console.log(`Todos count: ${count}`)
    // }, (err) => {
    //     console.log('unable to fetch todos', err)
    // })

    db.collection('Users').find({
        name: 'Stan'}).count().then((count) => {
        console.log(`Todos count: ${count}`)
    }, (err) => {
        console.log('unable to fetch todos', err)
    })


    //db.close()
})