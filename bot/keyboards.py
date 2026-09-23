from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from bot.constants import GRADES, OLYMPIAD_LOCATIONS


def subscription_keyboard(channel: str) -> InlineKeyboardMarkup:
    username = channel.lstrip("@")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Kanalga qo'shilish",
                    url=f"https://t.me/{username}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="A'zolikni tekshirish",
                    callback_data="check_subscription",
                )
            ],
        ]
    )


def registration_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ro'yxatdan o'tish")],
            [KeyboardButton(text="Sinov javoblarini jo'natish")],
        ],
        resize_keyboard=True,
    )


def registered_user_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Sinov javoblarini jo'natish")]],
        resize_keyboard=True,
    )


def contact_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Telefon raqamni ulashish", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def grades_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=grade)] for grade in GRADES],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def locations_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=location)] for location in OLYMPIAD_LOCATIONS],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def confirmation_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Tasdiqlayman")],
            [KeyboardButton(text="Qayta boshlash")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def remove_keyboard() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()
