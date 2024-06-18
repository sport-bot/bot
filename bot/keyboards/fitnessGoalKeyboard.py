from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def fitnessGoalKeyboard():
    keyboardBuilder = ReplyKeyboardBuilder()

    keyboardBuilder.button(text=_('Weight Loss'))
    keyboardBuilder.button(text=_('Muscle Gain'))
    keyboardBuilder.button(text=_('Improve Stamina'))
    keyboardBuilder.button(text=_('Maintenance of Fitness'))
    
    keyboardBuilder.adjust(2, 2)

    builder_markup = keyboardBuilder.as_markup()
    builder_markup.resize_keyboard = True

    return builder_markup