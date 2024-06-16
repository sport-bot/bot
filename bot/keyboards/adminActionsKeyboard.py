from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


adminActionsKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Add exercise')],
                                                [KeyboardButton(text='Add meal')],
                                                [KeyboardButton(text='Add meal recommendation')],
                                                [KeyboardButton(text='Add motivation frase')],
                                                [KeyboardButton(text='Return to main menu')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose admin action')