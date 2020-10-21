const fs = require('fs');
const _ = require('lodash')
const yargs = require('yargs')

const notes = require('./notes.js');

const titleOptions = {
    describe: 'Title of note',
    demand: true,
    alias: 't'
}

const bodyOptions = {
        describe: 'Body of note',
        demand: true,
        alias: 'b'
}
const argv = yargs
    .command('add', 'Add a new note', {
        title: titleOptions,
    body: bodyOptions
    })
    .command('list', 'List all notes')
    .command('read', 'Read a note',{
        title: titleOptions,
    })
    .command('remove', 'Remove a note',{
        title: titleOptions
    })
    .help()
    .argv
let command = argv._[0]

if (command === 'add') {
    var note = notes.addNote(argv.title, argv.body)
    if (note) {
        console.log('note created')
        notes.logNote(note)
    } else {
        console.log('note title taken')
    }

} else if (command === 'list') {
    var allNotes = notes.getAll();
    console.log(`printing ${allNotes.length} note(s)`)
    allNotes.forEach((note) => notes.logNote(note))
} else if (command === 'read') {
    notes.getNote(argv.title)
    var note = notes.getNote(argv.title)
    if (note) {
        console.log('note found')
        notes.logNote(note)
    } else {
        console.log('note is not found')
    }
} else if (command === 'remove') {
    notes.removeNote(argv.title)

} else {
    console.log('command not recognized')
}