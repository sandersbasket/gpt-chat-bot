import telebot
from telebot import types
from pyChatGPT import ChatGPT
from settings.settings import config
from keyboards import inline_keyboards as keyboards


api: ChatGPT = ChatGPT(config['session_token'])
bot: telebot.TeleBot = telebot.TeleBot(config['bot_token'])

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message) -> types.Message:
   return bot.send_message(message.chat.id, 'Commands: \n /new_question')


@bot.message_handler(commands=['new_question'])
def register_question(message: types.Message)  -> None:
    bot.send_message(message.chat.id, api.send_message('Hi i have a question!')['message'])
    bot.register_next_step_handler(message, answer_question)

def answer_question(message: types.Message) -> types.Message:
    return bot.send_message(message.chat.id, api.send_message(message.text)['message'].replace('`', ''), reply_markup = keyboards.question_buttons())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call) -> None:
    if call.data == 'continue':
        bot.edit_message_text(api.send_message('I have another question')['message'], call.message.chat.id, call.message.id)
        return bot.register_next_step_handler(call.message, answer_question)
    if call.data == 'reset':
        bot.edit_message_text('Success reset all questions!',call.message.chat.id, call.message.id)
        return api.clear_conversations()


def start_polling() -> None:
    return bot.infinity_polling()      