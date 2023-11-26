# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/amethyste.jpg?raw=true

# required: aiofiles, aiohttp, requests

import os
import logging
import aiohttp
import requests
import aiofiles

from .. import loader, utils

_list = [
    "3000years",
    "approved",
    "beautiful",
    "brazzers",
    "burn",
    "challenger",
    "circle",
    "contrast",
    "crush",
    "ddungeon",
    "dictator",
    "distort",
    "emboss",
    "fire",
    "frame",
    "afusion",
    "glitch",
    "greyscale",
    "instagram",
    "invert",
    "jail",
    "magik",
    "missionpassed",
    "moustache",
    "ps4",
    "posterize",
    "rejected",
    "rip",
    "scary",
    "scrolloftruth",
    "sepia",
    "sharpen",
    "sniper",
    "thanos",
    "trinity",
    "triggered",
    "unsharpen",
    "utatoo",
    "wanted",
    "wasted",
]

logger = logging.getLogger("Amethyste")


class Amethyste:
    def __init__(self, url) -> None:
        self.url = "https://v1.api.amethyste.moe"
        self.bearer = "747d367d03caf2cc850d5e8646ec3f3fffcea04c2b75fbce635bf9a771173a81d15ea1c1cb0bdecf0d53340994dd8a39647cd9f8c2fcf5bf833eaa6d65fac8ac"
        self.headers = {"Authorization": f"Bearer {self.bearer}"}
        self.data = {"url": url}

    async def request(self, template: str, **kwargs) -> dict:
        async with aiohttp.ClientSession() as session:
            final_url = f"{self.url}/generate/{template}"
            async with session.post(
                final_url, data=self.data, headers=self.headers, ssl=False
            ) as resp:
                data = await resp.content.read()
                logger.info(data)
                return data


async def oxo(file):
    re = requests.post("https://0x0.st", files={"file": file}, timeout=5)
    return re.text


@loader.module("Amethyste", "shizumods")
class AmethysteMod(loader.Module):
    """Make your pics fun and better with Amethyste :)"""

    strings = {
        "wait": "<emoji id=5787432469598835099>⏳</emoji> <b>Processing</b>...",
        "inv_args": "<emoji id=5800945811101585101>⚠️</emoji> <b>Invalid arguments</b>",
        "where_args": "<emoji id=5787657036258872916>📢</emoji> <b>Please, provide with arguments</b>",
        "available": "<emoji id=5780878813361606500>📀</emoji> <b>Available templates:</b>\n\n<code>{}</code>",
        "mustbephoto": "<emoji id=5787632606484893320>📸</emoji> <b>Reply to photo</b>",
    }

    strings_ru = {
        "wait": "<emoji id=5787432469598835099>⏳</emoji> <b>Обработка</b>...",
        "inv_args": "<emoji id=5800945811101585101>⚠️</emoji> <b>Неверные аргументы</b>",
        "where_args": "<emoji id=5787657036258872916>📢</emoji> <b>Пожалуйста, укажите аргументы</b>",
        "available": "<emoji id=5780878813361606500>📀</emoji> <b>Доступные шаблоны:</b>\n\n<code>{}</code>",
        "mustbephoto": "<emoji id=5787632606484893320>📸</emoji> <b>Ответьте на фото</b>",
    }

    strings_uz = {
        "wait": "<emoji id=5787432469598835099>⏳</emoji> <b>Yuklanmoqda</b>...",
        "inv_args": "<emoji id=5800945811101585101>⚠️</emoji> <b>Noto'g'ri argumentlar</b>",
        "where_args": "<emoji id=5787657036258872916>📢</emoji> <b>Iltimos, argumentlarni ko'rsating</b>",
        "available": "<emoji id=5780878813361606500>📀</emoji> <b>Mavjud shablonlar:</b>\n\n<code>{}</code>",
        "mustbephoto": "<emoji id=5787632606484893320>📸</emoji> <b>Fotoga javob bering</b>",
    }

    strings_jp = {
        "wait": "<emoji id=5787432469598835099>⏳</emoji> <b>処理中</b>...",
        "inv_args": "<emoji id=5800945811101585101>⚠️</emoji> <b>無効な引数</b>",
        "where_args": "<emoji id=5787657036258872916>📢</emoji> <b>引数を指定してください</b>",
        "available": "<emoji id=5780878813361606500>📀</emoji> <b>利用可能なテンプレート:</b>\n\n<code>{}</code>",
        "mustbephoto": "<emoji id=5787632606484893320>📸</emoji> <b>写真に返信してください</b>",
    }

    strings_ua = {
        "wait": "<emoji id=5787432469598835099>⏳</emoji> <b>Обробка</b>...",
        "inv_args": "<emoji id=5800945811101585101>⚠️</emoji> <b>Невірні аргументи</b>",
        "where_args": "<emoji id=5787657036258872916>📢</emoji> <b>Будь ласка, вкажіть аргументи</b>",
        "available": "<emoji id=5780878813361606500>📀</emoji> <b>Доступні шаблони:</b>\n\n<code>{}</code>",
        "mustbephoto": "<emoji id=5787632606484893320>📸</emoji> <b>Відповідь на фото</b>",
    }

    @loader.command()
    async def amet(self, app, message):
        """reply to photo with argument from templates list"""

        reply = message.reply_to_message

        if not reply or not reply.photo:
            return await utils.answer(message, self.strings["mustbephoto"])

        args = utils.get_args_raw(message)

        if not args:
            return await utils.answer(message, self.strings["where_args"])

        if args not in _list:
            return await utils.answer(message, self.strings["inv_args"])

        await utils.answer(message, self.strings["wait"])

        photo = await app.download_media(reply)

        async with aiofiles.open(photo, "rb") as f:
            data = await f.read()

        amethyste = Amethyste((await oxo(data)))

        async with aiofiles.open(f"{args}.png", "wb") as f:
            await f.write((await amethyste.request(args)))

        await utils.answer(
            message,
            f"{args}.png",
            photo_=True,
            caption=f"🩹 <b>Amethyste</b> | <code>{args}</code>",
        )

        os.remove(photo)
        os.remove(f"{args}.png")

    @loader.command()
    async def ametlist(self, app, message):
        """list of available templates for amet command"""
        await utils.answer(
            message,
            self.strings["available"].format(
                "\n".join([f"• <code>{i}</code>" for i in _list])
            ),
        )
