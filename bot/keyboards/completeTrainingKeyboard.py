from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

completeTrainingKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Complete training', callback_data='complete_training')],
])