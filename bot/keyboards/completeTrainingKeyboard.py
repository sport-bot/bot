from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def completeTrainingKeyboard():
    keyboardBuilder = InlineKeyboardBuilder()
    
    keyboardBuilder.button(text=_("Complete training", callback_data="complete_training"))

    return keyboardBuilder.as_markup()