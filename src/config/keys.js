require('dotenv').config();

module.exports = {
    telegramToken: process.env.TELEGRAM_TOKEN,
    mongoURI: process.env.MONGO_URI,
    googleClientID: process.env.GOOGLE_CLIENT_ID,
    googleClientSecret: process.env.GOOGLE_CLIENT_SECRET,
    googleRedirectURI: process.env.GOOGLE_REDIRECT_URI
};
