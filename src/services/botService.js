const Task = require('../models/Task');
const calendarService = require('./calendarService');

module.exports.handleStart = (bot, msg) => {
    bot.sendMessage(msg.chat.id, 'Welcome! This bot will help you manage your tasks and reminders.');
};

module.exports.createTask = (bot, msg, taskDetails) => {
    const [title, description, date] = taskDetails;
    const newTask = new Task({
        userId: msg.chat.id,
        title,
        description,
        date: new Date(date)
    });
    newTask.save().then(task => {
        calendarService.addEvent(task).then(event => {
            task.googleEventId = event.id;
            task.save().then(() => bot.sendMessage(msg.chat.id, 'Task created and added to Google Calendar.'));
        });
    });
};

module.exports.listTasks = (bot, msg) => {
    Task.find({ userId: msg.chat.id }).then(tasks => {
        let response = 'Your tasks:\n';
        tasks.forEach((task, index) => {
            response += `${index + 1}. ${task.title} - ${task.description} (Due: ${task.date})\n`;
        });
        bot.sendMessage(msg.chat.id, response);
    });
};

module.exports.editTask = (bot, msg, taskId, newDetails) => {
    const [title, description, date] = newDetails;
    Task.findByIdAndUpdate(taskId, { title, description, date: new Date(date) }, { new: true })
        .then(task => {
            calendarService.updateEvent(task.googleEventId, task).then(() => {
                bot.sendMessage(msg.chat.id, 'Task updated and changes reflected in Google Calendar.');
            });
        });
};

module.exports.deleteTask = (bot, msg, taskId) => {
    Task.findByIdAndRemove(taskId).then(task => {
        calendarService.deleteEvent(task.googleEventId).then(() => {
            bot.sendMessage(msg.chat.id, 'Task deleted and removed from Google Calendar.');
        });
    });
};
