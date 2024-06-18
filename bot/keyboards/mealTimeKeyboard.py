from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def mealTimeKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Breakfast'))
    keyboardBuilder.button(text=_('Lunch'))
    keyboardBuilder.button(text=_('Dinner'))
    
    keyboardBuilder.adjust(2, 1)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup
