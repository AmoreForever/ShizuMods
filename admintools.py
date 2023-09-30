# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


import logging


import html
import re

from typing import Union
from pyrogram import Client, types, errors
from datetime import datetime, timedelta

from .. import loader, utils


async def get_user(app: Client, args: str, reply: types.Message):
    extras = None

    if reply:
        user = await app.get_chat(reply.from_user.id)
        extras = args
    else:
        args_ = args.split()
        user = await app.get_chat(int(args_[0]) if args_[0].isdigit() else args_[0])
        if len(args_) < 2:
            user = await app.get_chat(int(args) if args.isdigit() else args)
        else:
            extras = args.split(maxsplit=1)[1]

    return user, extras


def process_time_args(duration_str):
    pattern = r"(\d+)([hmdyw])"
    match = re.match(pattern, duration_str)

    if not match:
        return False

    value = int(match[1])
    unit = match[2]
    if unit == "d":
        delta = timedelta(days=value)
    elif unit == "h":
        delta = timedelta(hours=value)
    elif unit == "m":
        delta = timedelta(minutes=value)
    elif unit == "s":
        delta = timedelta(seconds=value)
    elif unit == "y":
        delta = timedelta(days=value * 365)
    elif unit == "w":
        delta = timedelta(weeks=value)
    else:
        return False

    return datetime.now() + delta


@loader.module("AdminTools", "hikamoru", 1.1)
class AdminTools(loader.Module):
    """Free usefull admin tools"""

    strings = {
        "no_args_or_reply": "<emoji id=5807626765874499116>🚫</emoji> <b>No args or reply.</b>",
        "no_reply": "<emoji id=5807626765874499116>🚫</emoji> <b>No reply.</b>",
        "this_is_not_a_chat": "<emoji id=5807626765874499116>🚫</emoji> <b>This is not a chat.</b>",
        "cant_find_the_user": "<emoji id=5807626765874499116>🚫</emoji> <b>Can't find the user.</b>",
        "no_rights": "<emoji id=5818678700274617758>👮‍♀️</emoji> <b>No rights.</b>",
        "unknown_error": "<emoji id=5807626765874499116>🚫</emoji> Unknown error. See logs.",
        "the_user_is_an_admin": "<emoji id=5818678700274617758>👮‍♀️</emoji> <b>Error! The user is an admin.</b>",
        "kicked": "<emoji id=5346123695171580172>🏃</emoji><b>{name} was kicked.</b>\n<emoji id=6334541265077536138>❔</emoji> Reason: {reason}",
        "banned": "<emoji id=6334379984760604198>🔒</emoji> <b>{name} was banned.</b>\n<emoji id=6334541265077536138>❔</emoji> Reason: {reason}",
        "unbanned": "<emoji id=6334633031348782722>🔓</emoji> <b>{name} was unbanned.</b>\nReason: <emoji id=6334541265077536138>❔</emoji> {reason}",
        "muted": "<emoji id=6334460794570278986>🔇</emoji> <b>{name} was muted.</b>\n<emoji id=6334541265077536138>❔</emoji> Reason: <code>{reason}</code>",
        "tmuted": "<emoji id=6334460794570278986>🔇</emoji> <b>{name} was muted till</b> <code>{time}</code>.\n<emoji id=6334541265077536138>❔</emoji> Reason: {reason}",
        "unmuted": "<emoji id=6334513210351159296>🔊</emoji><b>{name} was unmuted.</b>\nReason: <emoji id=6334541265077536138>❔</emoji> {reason}",
        "pinned": "<emoji id=6334567936824444680>📌</emoji> <b>Message was pinned.</b>",
        "unpinned": "<emoji id=6334551070487873258>✂️</emoji> <b>Message was unpinned.</b>",
        "unpinned_all": "<emoji id=6334551070487873258>✂️</emoji> <b>All pinned messages were unpinned.</b>",
        "no_pin": "🙅‍♀️ <b>No pinned messages.</b>",
    }

    async def check_all(self, app: Client, message: types.Message, args: str):
        """Обработка всего"""
        chat = message.chat
        if chat.type == "private":
            return await utils.answer(message, self.strings["this_is_not_a_chat"])

        reply = message.reply_to_message
        if not (args or reply):
            return await utils.answer(message, self.strings["no_args_or_reply"])

        check_me = await app.get_chat_member(message.chat.id, self.tg_id)
        if not check_me.privileges.can_restrict_members:
            return await utils.answer(message, self.strings["no_rights"])

        try:
            return await get_user(app, args, reply)
        except errors.RPCError:
            return await utils.answer(message, self.strings["cant_find_the_user"])

    async def handle_mute_args(self, user: types.User, args: str = None):
        if not args:
            return (
                self.strings["muted"].format(
                    name=html.escape(utils.get_display_name(user)), reson="None"
                )
                + ".",
                None,
            )

        args_ = args.split("\n", maxsplit=1)
        args = args_[0]
        if not (n := process_time_args(args)):
            return (
                self.strings["muted"].format(
                    name=html.escape(utils.get_display_name(user)), reason=args
                ),
                None,
            )

        reason_text = args_[1] if len(args_) > 1 else None
        logging.info(reason_text)

        return (
            self.strings["tmuted"].format(
                name=html.escape(utils.get_display_name(user)),
                time=n,
                reason=reason_text or None,
            ),
            n,
        )

    @loader.command()
    async def kick(self, app: Client, message: types.Message):
        """Kick user. Usage: kick <@ or ID or reply> [reason]"""
        args = utils.get_args_raw(message)
        result = await self.check_all(app, message, args)
        if isinstance(result, list):
            return

        chat = message.chat

        user, reason = result
        try:
            await chat.ban_member(user.id)
            await chat.unban_member(user.id)
        except errors.UserAdminInvalid:
            return await utils.answer(message, self.strings["the_user_is_an_admin"])
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(
            message,
            self.strings["kicked"].format(
                name=html.escape(utils.get_display_name(user)), reason=reason or ""
            ),
        )

    @loader.command()
    async def ban(self, app: Client, message: types.Message):
        """Ban user. Usage: ban <@ or ID or reply> [reason]"""
        args = utils.get_args_raw(message)
        result = await self.check_all(app, message, args)
        if isinstance(result, list):
            return

        chat = message.chat

        user, reason = result
        try:
            await chat.ban_member(user.id)
        except errors.UserAdminInvalid:
            return await utils.answer(message, self.strings["the_user_is_an_admin"])
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(
            message,
            self.strings["banned"].format(
                name=html.escape(utils.get_display_name(user)), reason=reason or ""
            ),
        )

    @loader.command()
    async def unban(self, app: Client, message: types.Message):
        """Unban user. Usage: unban <@ or ID or reply>"""
        args = utils.get_args_raw(message)
        result = await self.check_all(app, message, args)
        if isinstance(result, list):
            return

        chat = message.chat

        user, reason = result
        try:
            await chat.unban_member(user.id)
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(
            message,
            self.strings["unbanned"].format(
                name=html.escape(utils.get_display_name(user)), reason=reason or ""
            ),
        )

    @loader.command()
    async def mute(self, app: Client, message: types.Message):
        """Mute user. Usage: mute <@ or ID or reply> [time (1m, 2h, 7d, etc.)] [*new line + reason]"""
        args = utils.get_args_raw(message)
        result = await self.check_all(app, message, args)
        if isinstance(result, list):
            return

        chat = message.chat

        user, args = result
        text, n = await self.handle_mute_args(user, args)

        try:
            if not n:
                await chat.restrict_member(
                    user.id, types.ChatPermissions(can_send_messages=False)
                )
            else:
                await chat.restrict_member(
                    user.id,
                    types.ChatPermissions(can_send_messages=False),
                    until_date=n,
                )
        except errors.UserAdminInvalid:
            return await utils.answer(message, self.strings["the_user_is_an_admin"])
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(message, text)

    @loader.command()
    async def unmute(self, app: Client, message: types.Message):
        """Unmute user. Usage: unmute <@ or ID or reply> [reason]"""
        args = utils.get_args_raw(message)
        result = await self.check_all(app, message, args)
        if isinstance(result, list):
            return

        chat = message.chat

        user, reason = result
        try:
            await chat.restrict_member(
                user.id, types.ChatPermissions(can_send_messages=True)
            )
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(
            message,
            self.strings["unmuted"].format(
                name=html.escape(utils.get_display_name(user)), reason=reason or "None"
            ),
        )

    @loader.command()
    async def pin(self, app: Client, message: types.Message):
        """Pin message. Usage: pin <reply>"""
        chat = message.chat

        if chat.type != "private":
            check_me = await app.get_chat_member(message.chat.id, self.tg_id)
            if not check_me.privileges.can_pin_messages:
                return await utils.answer(message, self.strings["no_rights"])

        reply = message.reply_to_message
        if not reply:
            return await utils.answer(message, self.strings["no_reply"])

        try:
            await reply.pin(True, True)
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(message, self.strings["pinned"])

    @loader.command()
    async def unpin(self, app: Client, message: types.Message):
        """Unpin message. Usage: unpin <reply> [all - unpin all]"""
        args = utils.get_args_raw(message)
        chat = message.chat

        if chat.type != "private":
            check_me = await app.get_chat_member(message.chat.id, self.tg_id)
            if not check_me.privileges.can_pin_messages:
                return await utils.answer(message, self.strings["no_rights"])

        chat = await app.get_chat(chat.id)
        pinned_message: Union[types.Message, None] = chat.pinned_message
        if not pinned_message:
            return await utils.answer(message, self.strings["no_pin"])

        try:
            if args == "all":
                await app.unpin_all_chat_messages(chat.id)
            else:
                await pinned_message.unpin()
        except errors.RPCError as error:
            logging.exception(error)
            return await utils.answer(message, self.strings["unknown_error"])

        return await utils.answer(
            message, self.strings["unpinned" if args != "all" else "unpinned_all"]
        )
