from flask import Flask, request
import telegram

token = '7706047778:AAEIIci7_LNix0RArwaVKwvubSiPidpf69k'

bot = telegram.Bot(token=token)
app = Flask(__name__)

@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot=bot)
        chat_id = update.effective_chat.id

        if update.message:
            text = update.message.text
            if 'test' in text:
                bot.send_message(chat_id=chat_id, text=f'Replying on a test message, message text=[{text}]')

        return 'OK'