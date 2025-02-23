import telebot

token = '7706047778:AAEIIci7_LNix0RArwaVKwvubSiPidpf69k'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello to gifbot!')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    # Get the message text
    text = message.text.lower()
    # Get the chat id
    chat_id = message.chat.id
    print(f'Message from {chat_id}: {text}')

    if 'test' in text:
        bot.send_message(chat_id, f'Replying on a test message, message text=[{text}]')


if __name__ == '__main__':
    try:
        print("Bot is polling. Press Ctrl+C to stop.")
        bot.polling(non_stop=True, interval=0)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        bot.stop_polling()
