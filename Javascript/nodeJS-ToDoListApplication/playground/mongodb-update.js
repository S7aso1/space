//const MongoClient = require('mongodb').MongoClient
const {MongoClient, ObjectID} = require('mongodb') //destructuring

MongoClient.connect('mongodb://localhost:27017/TodoApp',(err, db) =>{
    if(err){
        return console.log('unable to connect to mongo db server')
    }
    console.log('connected to mongo db server')

    // db.collection('Todos').findOneAndUpdate({
    //     _id: new ObjectID('5f8d663de6a41413c0552b5c')
    // }, {
    //     $set: {
    //         completed: true
    //     }
    // }, {
    //     returnOriginal: false
    // }).then((result) => {
    //     console.log(result)
    // })


    db.collection('Users').findOneAndUpdate({
        _id: new ObjectID('5f8d616f22e0ad2dc8a85649')
    }, {
        $set: {
            name: 'Stanislav'
        },
            $inc: {
                age: 1
            }
        }, {
        returnOriginal: false
    }).then((result) => {
        console.log(result)
    })





    //db.close()
})