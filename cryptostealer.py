# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/cryptostealer.jpg?raw=true

from pyrogram import Client, types

from .. import loader, utils


@loader.module("CryptoStealer", "shizumods")
class CryptoStealer(loader.Module):
    """Track crypto checkouts"""

    strings = {
        "stealed": "⛩ <b>Check successfully activated\n\n🔗 <a href='{}'>Check</a></b>",
        "disabled": "<emoji id=5854762571659218443>✅</emoji> <b>Stealer disabled</b>",
        "enabled": "<emoji id=5854762571659218443>✅</emoji> <b>Stealer enabled</b>",
    }

    strings_ru = {
        "stealed": "⛩ <b>Чек успешно активирован\n\n🔗 <a href='{}'>Чек</a></b>",
        "disabled": "<emoji id=5854762571659218443>✅</emoji> <b>Активатор отключен</b>",
        "enabled": "<emoji id=5854762571659218443>✅</emoji> <b>Активатор включен</b>",
    }

    strings_uz = {
        "stealed": "⛩ <b>Чек муваффақиятли активлаштирилди\n\n🔗 <a href='{}'>Чек</a></b>",
        "disabled": "<emoji id=5854762571659218443>✅</emoji> <b>Aktivator o'chirildi</b>",
        "enabled": "<emoji id=5854762571659218443>✅</emoji> <b>Aktivator yoqildi</b>",
    }

    strings_jp = {
        "stealed": "⛩ <b>チェックが正常にアクティブ化されました\n\n🔗 <a href='{}'>チェック</a></b>",
        "disabled": "<emoji id=5854762571659218443>✅</emoji> <b>アクティベーターが無効になっています</b>",
        "enabled": "<emoji id=5854762571659218443>✅</emoji> <b>アクティベーターが有効になっています</b>",
    }

    strings_ua = {
        "stealed": "⛩ <b>Чек успішно активований\n\n🔗 <a href='{}'>Чек</a></b>",
        "disabled": "<emoji id=5854762571659218443>✅</emoji> <b>Активатор вимкнено</b>",
        "enabled": "<emoji id=5854762571659218443>✅</emoji> <b>Активатор увімкнено</b>",
    }


    async def on_load(self, app: Client):
        if not self.db.get("shizu.stealer", "chat", None):
            chat = await utils.create_chat(
                app,
                "Shizu-CryptoSteals",
                "Here will be your crypto checkouts",
                True,
                True,
                True,
            )

            self.db.set("shizu.stealer", "chat", chat.id)

        chat = self.db.get("shizu.stealer", "chat", None)

        self.chat = chat

    async def watcher_crpyto(self, app: Client, message: types.Message):
        if (
            self.db.get("shizu.stealer", "status", True)
            and getattr(message, "via_bot", True)
            and getattr(message.via_bot, "usernames", None)
            and message.via_bot.usernames[0].username == "CryptoBot"
            and message.reply_markup
            and ("Check for" in message.text or "Чек на" in message.text)
        ):
            pre_url = message.reply_markup.inline_keyboard[0][0].url

            url = pre_url.split("http://t.me/CryptoBot?start=")[1]

            await app.send_message("Cryptobot", f"/start {url}")

            await self.bot.bot.send_message(
                self.chat, self.strings("stealed").format(pre_url)
            )

    @loader.command()
    async def stealer(self, app: Client, message: types.Message):
        """Enable or disable stealer"""

        if status := self.db.get("shizu.stealer", "status", True):
            self.db.set("shizu.stealer", "status", False)
            return await message.answer(self.strings("disabled"))

        self.db.set("shizu.stealer", "status", True)
        return await message.answer(self.strings("enabled"))
