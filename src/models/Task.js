const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const TaskSchema = new Schema({
    userId: String,
    title: String,
    description: String,
    date: Date,
    googleEventId: String
});

module.exports = mongoose.model('Task', TaskSchema);
