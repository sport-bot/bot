from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def genderKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Male'))
    keyboardBuilder.button(text=_('Female'))
    keyboardBuilder.button(text=_('Non-binary'))
    keyboardBuilder.button(text=_('Don`t specify'))
    
    keyboardBuilder.adjust(2, 2)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup