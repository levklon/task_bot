const { google } = require('googleapis');
const keys = require('../config/keys');

const oauth2Client = new google.auth.OAuth2(
    keys.googleClientID,
    keys.googleClientSecret,
    keys.googleRedirectURI
);

oauth2Client.setCredentials({
    refresh_token: 'your-refresh-token'
});

const calendar = google.calendar({ version: 'v3', auth: oauth2Client });

module.exports.addEvent = (task) => {
    return calendar.events.insert({
        calendarId: 'primary',
        requestBody: {
            summary: task.title,
            description: task.description,
            start: { dateTime: task.date },
            end: { dateTime: new Date(task.date.getTime() + 60 * 60 * 1000) }
        }
    }).then(response => response.data);
};

module.exports.updateEvent = (eventId, task) => {
    return calendar.events.update({
        calendarId: 'primary',
        eventId,
        requestBody: {
            summary: task.title,
            description: task.description,
            start: { dateTime: task.date },
            end: { dateTime: new Date(task.date.getTime() + 60 * 60 * 1000) }
        }
    }).then(response => response.data);
};

module.exports.deleteEvent = (eventId) => {
    return calendar.events.delete({
        calendarId: 'primary',
        eventId
    });
};
