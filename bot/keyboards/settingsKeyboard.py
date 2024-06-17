from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


settingsKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Change name'),
                                                  KeyboardButton(text='Change age')],
                                                [KeyboardButton(text='Change weight'),
                                                KeyboardButton(text='Change height')],
                                                [KeyboardButton(text='Change fitness lvl'),
                                                KeyboardButton(text='Change goal')],
                                                [KeyboardButton(text='Save settings changes')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose settings...')
