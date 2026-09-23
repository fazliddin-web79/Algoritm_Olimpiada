import logging
from typing import Optional

from aiogram import Bot
from aiogram.enums import ChatMemberStatus
from aiogram.exceptions import TelegramAPIError


logger = logging.getLogger(__name__)


def has_active_membership(status: ChatMemberStatus, is_member: bool = False) -> bool:
    return status in {
        ChatMemberStatus.CREATOR,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.MEMBER,
    } or (status == ChatMemberStatus.RESTRICTED and is_member)


async def is_channel_member(
    bot: Bot,
    channel: str,
    user_id: int,
) -> Optional[bool]:
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
    except TelegramAPIError:
        logger.exception("Kanal a'zoligini tekshirib bo'lmadi: %s", channel)
        return None
    return has_active_membership(
        member.status,
        bool(getattr(member, "is_member", False)),
    )
