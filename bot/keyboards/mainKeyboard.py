from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mainKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Receive a training'),
                                                KeyboardButton(text='Settings')]],
                            resize_keyboard=True,
                            input_field_placeholder='Choose action')
