from telebot import TeleBot
import emoji
import time
from diffi_algorythm import DH_Endpoint
TOKEN = 'BOT_TOKEN'
bot = TeleBot(TOKEN)
nout = DH_Endpoint()
dec_id = 0
enc_id = 0
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hi)\nI can encrypted or decrypted your text.' + emoji.emojize(':man_technologist:')
                     +'\nIf you have question then input command /help or choose it in menu.')

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'The bot is designed to learn how the Diffie Hellman encryption algorithm works.'
                                      '\nSo that you can learn the algorithm, enter the /study command.'
                                      '\nIn order for you to be able to encrypt the text, enter the /encrypt command.'
                                      '\nIn order for you to be able to decrypt the text, enter the /decrypt command.')

@bot.message_handler(commands=["study"])
def study(message):
    bot.send_photo(message.chat.id, photo=open('Diffie.jpg', 'rb'))

@bot.message_handler(commands=["encrypt"])
def encrypt(message):
    global enc_id
    enc_id = message.message_id
    bot.send_message(message.chat.id, 'Input your text')

@bot.message_handler(commands=["decrypt"])
def decrypt(message):
    global dec_id
    dec_id = message.message_id
    bot.send_message(message.chat.id, 'Input your text')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    global dec_id
    global enc_id
    message.message_id -= 1

    if (dec_id == message.message_id - 1):
        bot.send_message(message.chat.id, 'Decryption process...')
        time.sleep(2.5)
        dec = nout.decrypt_message(message.text)
        bot.send_message(message.chat.id, dec)

    if (enc_id == message.message_id - 1):
        bot.send_message(message.chat.id, 'Encryption process...')
        time.sleep(2.5)
        nout_full = nout.generate_full_key()
        enc = nout.encrypt_message(message.text) + '&' + chr(nout_full)
        bot.send_message(message.chat.id, enc)

bot.polling(none_stop=True, interval=0)
