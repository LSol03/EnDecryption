from telebot import TeleBot
import emoji
import time
from diffi_algorythm import DH_Endpoint
import base64
TOKEN = 'bot token'
bot = TeleBot(TOKEN)
nout = DH_Endpoint()
dec_id = 0
enc_id = 0
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hi)\nI can encrypted or decrypted your text.' + emoji.emojize(':man_technologist:')
                     +'\nIf you have question then input command /help or choose it in menu.')
    global nout

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
    bot.send_message(message.chat.id, 'Input your txt/img/doc')

@bot.message_handler(commands=["decrypt"])
def encrypt(message):
    global dec_id
    dec_id = message.message_id
    bot.send_message(message.chat.id, 'Input your txt/img/doc')

@bot.message_handler(func=lambda m: True, content_types=['photo'])
def get_broadcast_picture(message):
    file_path = bot.get_file(message.photo[0].file_id).file_path
    file = bot.download_file(file_path)
    with open("python1.png", "wb") as code:
        code.write(file)
    with open("python1.png", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    with open('encode.bin', "wb") as file:
        file.write(converted_string)

    file = open('encode.bin', 'rb')
    byte = file.read()
    file.close()

    decodeit = open('hello_level.jpeg', 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()

    bot.send_message(message.chat.id, 'Encryption process...')
    time.sleep(2.5)
    with open("encode.bin", "rb") as misc:
        f = misc.read()
    bot.send_document(message.chat.id, f)

@bot.message_handler(content_types=["document"])
def get_doc(message):
    bot.send_message(message.chat.id, 'Decryption process...')
    time.sleep(2.5)
    bot.send_photo(message.chat.id, photo=open('hello_level.jpeg', 'rb'))

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
