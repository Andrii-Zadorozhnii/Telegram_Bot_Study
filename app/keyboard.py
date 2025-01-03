from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Trash box')],
                                     [KeyboardButton(text='Contacts'),
                                     KeyboardButton(text='About As')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose menu button...')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='T-Shirts', callback_data = 't-shirts')],
    [InlineKeyboardButton(text='Sneakers', callback_data = 'sneakers')],
    [InlineKeyboardButton(text='Cap', callback_data = 'cap')]
])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send number',
                                                           request_contact=True)]],
                                 resize_keyboard=True)

