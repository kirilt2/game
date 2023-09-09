import asyncio
from telegram import Bot, Update, ForceReply, InputFile
from telegram.ext import Updater, CommandHandler, Application, ContextTypes

bot_token = '6660902386:AAGbERi4TQa4MWFSfe2AdaEFRt9X49RcA2s'

bot = Bot(token=bot_token)

class MyBot:
    def __init__(self, bot_token):
        self.application = Application.builder().token(bot_token).build()

        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("memes", self.send_multiple_memes))
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        await update.message.reply_text(
            f"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(text="Это простой бот. Он может отвечать на текстовые сообщения.")

    async def send_multiple_memes(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
      
        memes = ['meme1.jpeg', 'meme2.jpg', 'meme.jpeg', 'meme1.jpeg', 'meme2.jpg', 'meme.jpeg', 'meme1.jpeg', 'meme2.jpg', 'meme.jpeg', 'meme1.jpeg', 'meme2.jpg', 'meme.jpeg','meme1.jpeg', 'meme2.jpg', 'meme.jpeg','meme1.jpeg', 'meme2.jpg', 'meme.jpeg','meme1.jpeg', 'meme2.jpg', 'meme.jpeg','meme1.jpeg', 'meme2.jpg', 'meme.jpeg'] 
        for meme_file_name in memes:
            with open(meme_file_name, 'rb') as meme_file:
                await update.message.reply_photo(photo=InputFile(meme_file))

if __name__ == "__main__":
    bot = MyBot(bot_token=bot_token)
