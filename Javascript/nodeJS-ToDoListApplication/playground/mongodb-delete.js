//const MongoClient = require('mongodb').MongoClient
const {MongoClient, ObjectID} = require('mongodb') //destructuring

MongoClient.connect('mongodb://localhost:27017/TodoApp',(err, db) =>{
    if(err){
        return console.log('unable to connect to mongo db server')
    }
    console.log('connected to mongo db server')

    // db.collection('Todos').deleteMany({text: 'eat'}).then((result) => {
    //     console.log(result)
    // })

    // db.collection('Users').deleteMany({name: 'Stan'}).then((result) => {
    //     console.log(result)
    // })

    // db.collection('Todos').deleteOne({text: 'eat'}).then((result) => {
    //     console.log(result)
    // })

    // db.collection('Todos').findOneAndDelete({completed: false}).then((result) => {
    //     console.log(result)
    // })

    db.collection('Users').findOneAndDelete({_id: new ObjectID('5f8d63585250722288e28b87')}).then((result) => {
        console.log(JSON.stringify(result, undefined, 2))
    })

    //db.close()
})