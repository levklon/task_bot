const express = require('express');
const router = express.Router();

// Load Task model
const Task = require('../models/Task');

// @route   GET api/tasks/test
// @desc    Tests tasks route
// @access  Public
router.get('/test', (req, res) => res.json({ msg: 'Tasks Works' }));

// @route   POST api/tasks
// @desc    Create a task
// @access  Public
router.post('/', (req, res) => {
    const newTask = new Task({
        userId: req.body.userId,
        title: req.body.title,
        description: req.body.description,
        date: req.body.date
    });
    newTask.save().then(task => res.json(task));
});

// @route   GET api/tasks
// @desc    Get all tasks
// @access  Public
router.get('/', (req, res) => {
    Task.find().then(tasks => res.json(tasks));
});

// @route   PUT api/tasks/:id
// @desc    Update a task
// @access  Public
router.put('/:id', (req, res) => {
    Task.findByIdAndUpdate(req.params.id, req.body, { new: true })
        .then(task => res.json(task));
});

// @route   DELETE api/tasks/:id
// @desc    Delete a task
// @access  Public
router.delete('/:id', (req, res) => {
    Task.findByIdAndRemove(req.params.id)
        .then(task => res.json({ success: true }));
});

module.exports = router;
