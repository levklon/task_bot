from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, CallbackContext
from .commands import (
    start, add_task_start, add_task, update_task_start,
    update_task, save_updated_task, delete_task_start, delete_task, view_tasks, cancel, unknown_command,
    ADD_TASK, UPDATE_TASK, DELETE_TASK, VIEW_TASKS
)

def start_bot(token):
    application = Application.builder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("add", add_task_start),
            CommandHandler("update", update_task_start),
            CommandHandler("delete", delete_task_start),
            CommandHandler("view", view_tasks)
        ],
        states={
            ADD_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_task)],
            UPDATE_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, update_task)],
            UPDATE_TASK + 1: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_updated_task)],
            DELETE_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, delete_task)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    application.run_polling()

async def handle_text(update: Update, context: CallbackContext):
    user = update.message.from_user
    if 'started' not in context.user_data:
        context.user_data['started'] = True
        await start(update, context)
    else:
        await unknown_command(update, context)
