const fs = require('fs')


var fetchNotes = () => {
    try { // Tries to load a file; if it's absent or with corrupted data it will throw an error which will be handled by catch
        var notesString = fs.readFileSync('notes-data.json')
        return JSON.parse(notesString)
    } catch (e) {//
        return []
    }
}

var saveNotes = (notes) => {
    fs.writeFileSync('notes-data.json', JSON.stringify(notes))
}

var addNote = (title, body) => {
    var notes = fetchNotes()
    var note = {
        title: title,
        body: body
    }
    var duplicateNotes = notes.filter((note) => /* return true if they match*/ note.title === title)

    if (duplicateNotes.length === 0) {
        notes.push(note)
        saveNotes(notes)
        return note
    }

}

var getAll = () => {
    return fetchNotes()
}

var getNote = (title) => {
    var notes = fetchNotes()
    var filteredNotes = notes.filter((note) => /*return true if they match*/ note.title === title)
    return filteredNotes[0]
}

var removeNote = (title) => {
    var notes = fetchNotes()
    var filteredNotes = notes.filter((note) => /* return true if they don't match*/ note.title !== title)
    saveNotes(filteredNotes)

    if(notes.length == filteredNotes.length){
        console.log('note was not found')
    }else{
        console.log('note was removed')
    }
}

var logNote = (note) => {
    console.log('------------')
    console.log(`Title: ${note.title}`)
    console.log(`Body: ${note.body}`)
}

module.exports = {
    addNote: addNote,
    getAll: getAll,
    getNote: getNote,
    removeNote: removeNote,
    logNote: logNote
}