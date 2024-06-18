
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def settingsKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Change name'))
    keyboardBuilder.button(text=_('Change age'))
    keyboardBuilder.button(text=_('Change weight'))
    keyboardBuilder.button(text=_('Change height'))
    keyboardBuilder.button(text=_('Change fitness lvl'))
    keyboardBuilder.button(text=_('Change goal'))
    keyboardBuilder.button(text=_('⬅️ Back to main menu'))
    keyboardBuilder.button(text=_('Change language'))
    
    keyboardBuilder.adjust(2, 2, 2, 2)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup
