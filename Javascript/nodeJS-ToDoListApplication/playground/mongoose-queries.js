const {ObjectID, ObjectId} = require('mongodb')

const {mongoose} = require('./../server/db/mongoose')
const {Todo} = require('./../server/models/todo')
const {User} = require('./../server/models/user')
var id = '5f8ea49874cfd59816c4ef4d'

// if(!ObjectId.isValid(id)){
//     console.log('id is unvalid')
// }

// Todo.find({
//     _id: id
// }).then((todos) => {
//     console.log('Todos', todos)
// })

// Todo.findOne({
//     _id: id
// }).then((todo) => {
//     console.log('Todo', todo)
// })

// Todo.findById(id).then((todo) => {
//     if(!todo){
//         return console.log('id not found')
//     }
//     console.log('todo by id', todo)
// }).catch((e) => console.log(e))

User.findById(id).then((user) => {
    if(!user){
        return console.log('user not found')
    }
    console.log('user by id', JSON.stringify(user, undefined, 2))
}).catch((e) => console.log(e))