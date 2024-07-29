from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from db.database import add_task_to_db, update_task_in_db, delete_tasks_from_db, get_tasks_from_db


ADD_TASK, UPDATE_TASK, DELETE_TASK, VIEW_TASKS = range(4)


COMMANDS = [
    ["/add", "/update", "/delete", "/view"]
]

async def start(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(COMMANDS, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to Task Bot! Choose a command:",
        reply_markup=keyboard
    )

async def add_task_start(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter the task you want to add:", reply_markup=ReplyKeyboardRemove())
    return ADD_TASK

async def add_task(update: Update, context: CallbackContext):
    task = update.message.text
    add_task_to_db(task)
    await update.message.reply_text(f"Task '{task}' added!")
    await show_commands(update, context)
    return ConversationHandler.END

async def update_task_start(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter the task number you want to update:", reply_markup=ReplyKeyboardRemove())
    return UPDATE_TASK

async def update_task(update: Update, context: CallbackContext):
    task_number = int(update.message.text)
    context.user_data['task_number'] = task_number
    await update.message.reply_text("Please enter the new task:")
    return UPDATE_TASK + 1

async def save_updated_task(update: Update, context: CallbackContext):
    new_task = update.message.text
    task_number = context.user_data['task_number']
    update_task_in_db(task_number, new_task)
    await update.message.reply_text(f"Task number {task_number} updated to '{new_task}'!")
    await show_commands(update, context)
    return ConversationHandler.END

async def delete_task_start(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter the task numbers you want to delete (comma separated):", reply_markup=ReplyKeyboardRemove())
    return DELETE_TASK

async def delete_task(update: Update, context: CallbackContext):
    task_numbers = list(map(int, update.message.text.split(',')))
    delete_tasks_from_db(task_numbers)
    await update.message.reply_text(f"Tasks {', '.join(map(str, task_numbers))} deleted!")
    await show_commands(update, context)
    return ConversationHandler.END

async def view_tasks(update: Update, context: CallbackContext):
    tasks = get_tasks_from_db()
    task_list = "\n".join([f"{number}. {task}" for number, task in tasks])
    await update.message.reply_text(task_list)
    await show_commands(update, context)
    return ConversationHandler.END

async def show_commands(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(COMMANDS, resize_keyboard=True)
    await update.message.reply_text(
        "Choose a command:",
        reply_markup=keyboard
    )

async def unknown_command(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(COMMANDS, resize_keyboard=True)
    await update.message.reply_text(
        "Sorry, please choose an existing command from the keyboard.",
        reply_markup=keyboard
    )

def cancel(update: Update, context: CallbackContext):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text='Operation cancelled.')
    return ConversationHandler.END
