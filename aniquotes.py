# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/aniquotes.jpg?raw=true

import random

from pyrogram.types import Sticker
from pyrogram import Client

from .. import loader, utils


@loader.module("AnimatedQuotes", "shizumods")
class AnimatedQuotes(loader.Module):
    """Animated quotes for fun"""

    @loader.command()
    async def tyq(self, app: Client, message):
        """Mini tyan quotes"""
        args = utils.get_args_raw(message)
        reply = message.reply_to_message
        if not args:
            return await message.answer(
                "<emoji id=6332121420373428086>😤</emoji> <b>Please provide arguments.</b>"
            )
        result = (
            (await app.get_inline_bot_results("@quotafbot", args))
            .results[random.randint(0, 2)]
            .document
        )
        sticker = await Sticker._parse(
            client=app,
            sticker=result,
            document_attributes={type(i): i for i in result.attributes},
        )
        await message.delete()
        await app.send_sticker(
            message.chat.id,
            sticker.file_id,
            reply_to_message_id=reply.id if reply else None,
        )

    @loader.command()
    async def frq(self, app: Client, message):
        """Clown frog quotes""" ""
        args = utils.get_args_raw(message)
        reply = message.reply_to_message
        if not args:
            return await message.answer(
                "<emoji id=6332121420373428086>😤</emoji> <b>Please provide arguments.</b>"
            )
        result = (
            (await app.get_inline_bot_results("@honka_says_bot", f"{args}."))
            .results[0]
            .document
        )
        sticker = await Sticker._parse(
            client=app,
            sticker=result,
            document_attributes={type(i): i for i in result.attributes},
        )
        await message.delete()
        await app.send_sticker(
            message.chat.id,
            sticker.file_id,
            reply_to_message_id=reply.id if reply else None,
        )

    @loader.command()
    async def twq(self, app: Client, message):
        """Twitter status quotes"""
        args = utils.get_args_raw(message)
        reply = message.reply_to_message
        if not args:
            return await message.answer(
                "<emoji id=6332121420373428086>😤</emoji> <b>Please provide arguments.</b>"
            )
        result = (
            (await app.get_inline_bot_results("@TwitterStatusBot", args))
            .results[0]
            .document
        )
        sticker = await Sticker._parse(
            client=app,
            sticker=result,
            document_attributes={type(i): i for i in result.attributes},
        )
        await message.delete()
        await app.send_sticker(
            message.chat.id,
            sticker.file_id,
            reply_to_message_id=reply.id if reply else None,
        )
