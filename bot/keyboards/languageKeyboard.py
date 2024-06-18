from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.db.models.LanguageModel import Language

def languageKeyboard(languages: list[Language]):
    
    keyboardBuilder = ReplyKeyboardBuilder()

    for i in range(len(languages)):
        keyboardBuilder.button(text=languages[i].code)
    

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup