from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


adminActionsKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Add exercise')],
                                                [KeyboardButton(text='Add product')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose admin action')
