from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _


def generate_training_navigation_buttons(current_index: int, amount: int):
    keyboardBuilder = InlineKeyboardBuilder()

    for i in range(amount):
        keyboardBuilder.button(text=f'{i+1}', callback_data=f"training_{i}")

    keyboardBuilder.button(text=_("Select"), callback_data=f"select_training_{current_index}")
    keyboardBuilder.adjust(amount, 1)
    return keyboardBuilder.as_markup()