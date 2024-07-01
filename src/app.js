const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const keys = require('./config/keys');

const app = express();

// Bodyparser Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(keys.mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB Connected'))
    .catch(err => console.log(err));

// Use Routes
const tasks = require('./routes/tasks');
app.use('/api/tasks', tasks);

const port = process.env.PORT || 5000;
app.listen(port, () => console.log(`Server running on port ${port}`));
