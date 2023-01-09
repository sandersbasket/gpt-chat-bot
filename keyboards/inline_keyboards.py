from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def question_buttons() -> InlineKeyboardMarkup:
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Continue", callback_data = "continue"), InlineKeyboardButton("Reset", callback_data = "reset"))
    return markup