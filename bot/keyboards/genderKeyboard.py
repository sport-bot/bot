from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


genderKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Male'),
                                                KeyboardButton(text='Female')],
                                                [KeyboardButton(text='Non-binary'),
                                                KeyboardButton(text='Don`t specify')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose your gender')


# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
#     [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
#     [InlineKeyboardButton(text='Кепки', callback_data='cap')]])


# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
#                                                            request_user=True)]],
#                                  resize_keyboard=True)