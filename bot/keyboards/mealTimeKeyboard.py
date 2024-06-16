from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mealTimeKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Breakfast'),
                                                KeyboardButton(text='Lunch')],
                                                [KeyboardButton(text='Dinner')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose meal time...')
