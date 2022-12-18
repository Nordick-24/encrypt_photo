from stegano import lsb
import os
import telebot


def unhide_image(bot, message):
    result = lsb.reveal("secret.png")
    bot.send_message(message.chat.id, result)


api_token = os.getenv("api_token2")
bot_unhide = telebot.TeleBot(api_token)


@bot_unhide.message_handler(commands=['start'])
def start(message):
    bot_unhide.send_message(message.chat.id, "Send image: ")


    @bot_unhide.message_handler(content_types=['photo'])
    def get_user_photo(message) -> None:
        """Download Photo with the text from user."""
        fileID = message.photo[-1].file_id
        file_info = bot_unhide.get_file(fileID)
        downloaded_file = bot_unhide.download_file(file_info.file_path)

        with open("not_secret.jpg", "wb") as newfile:
            newfile.write(downloaded_file)

        unhide_image(bot_unhide, message)




