from telegram.ext import ApplicationBuilder, CommandHandler

import sqlalchemy as db

from controllers import HelloController
from services import ConfigurationService

ConfigurationService = ConfigurationService('DEFAULT')

engine = db.create_engine(ConfigurationService.return_value("DB_CONNECTION"))
connection = engine.connect()


app = ApplicationBuilder().token(ConfigurationService.return_value("TOKEN")).build()

app.add_handler(CommandHandler("hello", HelloController.hello))

app.run_polling()