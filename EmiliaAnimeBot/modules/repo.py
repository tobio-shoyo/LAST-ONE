from EmiliaAnimeBot import dispatcher

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext
from telegram.ext.dispatcher import  run_async

GIT_PIC = "https://telegra.ph/file/311df2003dc985a39ddf6.jpg"

GIT_TEXT = """
Hinata Shōyō Robot By @INTERVIER_RRRR

*Contributors/Credits*

> [IzumiCypherX](https://github.com/IzumiCypherX)

"""

@run_async
def repo(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        GIT_PIC,
        caption = GIT_TEXT,
        parse_mode=ParseMode.MARKDOWN
        )

REPO_HANDLER = CommandHandler("repo", repo)

dispatcher.add_handler(REPO_HANDLER)
