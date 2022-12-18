from threading import Thread
from unhiden_bot import *
from hiden_bot import *


th1 = Thread(target=bot.polling)
th2 = Thread(target=bot_unhide.polling)

if __name__ == '__main__':
    th1.start()
    th2.start()

