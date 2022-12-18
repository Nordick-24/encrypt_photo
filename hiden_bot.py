from stegano import lsb
import os
import telebot


def hiden_image(text: str, bot, message):
    hiden_image = lsb.hide('not_secret.jpg', text)
    hiden_image.save("secret.png")

    with open('secret.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)



api_token = os.getenv('api_token')
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Welcome, for start send your image: ", parse_mode='html')

    @bot.message_handler(content_types=['photo'])
    def get_user_photo(message) -> None:
        """Download Photo with the text from user."""
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("not_secret.jpg", "wb") as newfile:
            newfile.write(downloaded_file)

        bot.send_message(message.chat.id, "Enter secret text: ")

        @bot.message_handler()
        def user_secret_text(message):
            hiden_image(message.text, bot, message)

