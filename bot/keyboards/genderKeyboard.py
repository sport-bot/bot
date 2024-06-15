from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


genderKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Male'),
                                                KeyboardButton(text='Female')],
                                                [KeyboardButton(text='Non-binary'),
                                                KeyboardButton(text='Don`t specify')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose your gender')
