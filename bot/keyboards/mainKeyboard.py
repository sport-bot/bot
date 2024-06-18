from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def mainKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Receive a training'))
    keyboardBuilder.button(text=_('Settings'))
    
    keyboardBuilder.adjust(2)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup