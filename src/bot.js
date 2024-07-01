const TelegramBot = require('node-telegram-bot-api');
const keys = require('./config/keys');
const botService = require('./services/botService');

const bot = new TelegramBot(keys.telegramToken, { polling: true });

bot.onText(/\/start/, (msg) => {
    botService.handleStart(bot, msg);
});

bot.onText(/\/newtask (.+)/, (msg, match) => {
    const taskDetails = match[1].split('|');
    botService.createTask(bot, msg, taskDetails);
});

bot.onText(/\/tasks/, (msg) => {
    botService.listTasks(bot, msg);
});

bot.onText(/\/edittask (\d+) (.+)/, (msg, match) => {
    const taskId = match[1];
    const newDetails = match[2].split('|');
    botService.editTask(bot, msg, taskId, newDetails);
});

bot.onText(/\/deletetask (\d+)/, (msg, match) => {
    const taskId = match[1];
    botService.deleteTask(bot, msg, taskId);
});

module.exports = bot;
