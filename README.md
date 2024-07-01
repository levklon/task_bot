# Task Management and Reminder Bot with Google Calendar Integration


## Overview

Welcome to the Task Management and Reminder Bot project! This Telegram bot helps you manage your tasks and reminders with seamless integration into Google Calendar. Create, edit, and delete tasks, and receive reminders for upcoming tasks. All tasks are synchronized with Google Calendar for easy access and management.

## Features

- **User Registration:** Start using the bot with the `/start` command.
- **Create Tasks:** Create new tasks using the `/newtask` command.
- **View Tasks:** View your tasks with the `/tasks` command.
- **Edit Tasks:** Edit existing tasks using the `/edittask` command.
- **Delete Tasks:** Delete tasks using the `/deletetask` command.
- **Google Calendar Integration:** Synchronize tasks with Google Calendar.
- **Reminders:** Receive reminders for your tasks.

## Technologies Used

- **Node.js:** JavaScript runtime for building server-side applications.
- **Express:** Fast, unopinionated, minimalist web framework for Node.js.
- **MongoDB:** NoSQL database for storing tasks.
- **Telegram Bot API:** Interface for building Telegram bots.
- **Google Calendar API:** Interface for integrating with Google Calendar.

## Installation

### Prerequisites

- Node.js and npm installed on your system.
- MongoDB instance (local or cloud).
- Google API credentials for Google Calendar integration.
- Telegram Bot Token.

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task_bot.git
    cd task_bot
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Create a `.env` file in the root directory and add the following environment variables:

    ```plaintext
    TELEGRAM_TOKEN=your-telegram-bot-token
    MONGO_URI=your-mongodb-uri
    GOOGLE_CLIENT_ID=your-google-client-id
    GOOGLE_CLIENT_SECRET=your-google-client-secret
    GOOGLE_REDIRECT_URI=your-google-redirect-uri
    ```

4. Start the server and the bot:

    ```bash
    node src/app.js
    node src/bot.js
    ```

## Usage

1. **Register with the bot:**

   Open your Telegram app, find your bot, and send the `/start` command.

2. **Create a new task:**

   Use the `/newtask` command followed by the task details:

   /newtask Task Title | Task Description | YYYY-MM-DDTHH:MM

   Example:

   /newtask Finish project report | Complete the final report for the project | 2024-07-05T10:00:00

3. **View your tasks:**

   Send the `/tasks` command to the bot.

4. **Edit a task:**

   Use the `/edittask` command followed by the task ID and new details:

   /edittask task_id Task Title | Task Description | YYYY-MM-DDTHH:MM

   Example:

   /edittask 1 Update project report | Make final revisions to the project report | 2024-07-06T14:00:00


5. **Delete a task:**

   Use the `/deletetask` command followed by the task ID:

   /deletetask task_id

   Example:

   /deletetask 1



## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

---

Thank you for checking out the Task Management and Reminder Bot project! If you find it useful, please give it a star and share it with others.

