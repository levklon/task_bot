# Task Bot

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)

## Overview  

The **Task Bot** is a Telegram bot designed to help users manage their tasks efficiently. It allows users to add, update, delete, and view their tasks directly within Telegram. Built with Python and MongoDB, this bot provides a simple yet powerful task management solution.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- View all tasks

## Technologies Used
 
- **Programming Language**: Python
- **Database**: MongoDB
- **APIs**: Telegram Bot API 

## Installation

### Prerequisites

- Python 3.x
- MongoDB
- Telegram Bot Token

### Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/levklon/task_bot.git
    cd task_bot
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure environment variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your Telegram Bot Token to the `.env` file as follows:
      ```sh
      TELEGRAM_BOT_TOKEN=your_telegram_bot_token
      MONGODB_URI=your_mongodb_uri
      ```

5. **Start the bot**:
    ```sh
    python main.py
    ```

## Usage

- Open Telegram and start a chat with your bot.
- Add, update, delete, and view tasks using bot commands.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

