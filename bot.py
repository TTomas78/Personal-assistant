from telegram.ext import ApplicationBuilder, CommandHandler

import sqlalchemy as db

from controllers.hello import HelloController

engine = db.create_engine('')
connection = engine.connect()


app = ApplicationBuilder().token("-").build()

app.add_handler(CommandHandler("hello", HelloController.hello))

app.run_polling()