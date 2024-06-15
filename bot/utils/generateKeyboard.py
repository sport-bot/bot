from aiogram.utils.keyboard import InlineKeyboardBuilder

def generate_training_navigation_buttons(current_index: int, amount: int):
    keyboardBuilder = InlineKeyboardBuilder()

    for i in range(amount):
        keyboardBuilder.button(text=f'{i+1}', callback_data=f"training_{i}")

    keyboardBuilder.button(text="Select", callback_data=f"select_training_{current_index}")
    keyboardBuilder.adjust(6, 1)
    return keyboardBuilder.as_markup()