
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def adminActionsKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Add exercise'))
    keyboardBuilder.button(text=_('Add meal'))
    keyboardBuilder.button(text=_('Add meal recommendation'))
    keyboardBuilder.button(text=_('Add motivation frase'))
    keyboardBuilder.button(text=_('Add new language'))
    keyboardBuilder.button(text=_('Return to main menu'))
    
    keyboardBuilder.adjust(1, 1, 1, 1, 1, 1)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup