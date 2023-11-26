# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/usertools.jpg?raw=true

import datetime

import asyncio

from pyrogram import Client, types, enums

from .. import loader, utils


class Elevator(dict):
    def __missing__(self, key):
        return 0


@loader.module(name="UserTools", author="shizumods")
class UserTools(loader.Module):
    """This module for see stats of your chat(s)"""

    strings = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>Processing...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>Here is the list of most frequently used words in this chat:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>Your statistics acquired within <code>{}</code> seconds.</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>You have <code>{}</code> private chats</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>You have {} Bots</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>You are in <code>{}</code> Groups</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>You are in <code>{}</code> Supergroups</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>You are in <code>{}</code> Channels</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>You are admin in <code>{}</code> Chats </b>\n"
        ),
    }

    strings_ru = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>Обработка...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>Вот список самых часто используемых слов в этом чате:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>Статистика получена за <code>{}</code> секунд.</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>У вас <code>{}</code> личных чатов</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>У вас {} ботов</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Вы в <code>{}</code> группах</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Вы в <code>{}</code> супергруппах</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>Вы в <code>{}</code> каналах</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>Вы админ в <code>{}</code> чатах </b>\n"
        ),
    }

    strings_uz = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>Procesda...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>Bu chatda eng ko'p ishlatiladigan so'zlarning ro'yxati:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>Statistika <code>{}</code> soniyada olingan.</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>Sizda <code>{}</code> ta shaxsiy chatlar mavjud</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>Sizda {} ta botlar mavjud</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Siz <code>{}</code> guruhlarda</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Siz <code>{}</code> superguruhlarda</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>Siz <code>{}</code> kanallarda</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>Siz <code>{}</code> chatda admin </b>\n"
        ),
    }

    strings_jp = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>処理中...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>ここにこのチャットで最もよく使われている単語のリストがあります:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>統計情報は<code>{}</code>秒で取得されます。</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>個人チャット<code>{}</code>個</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>ボット<code>{}</code>個</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>グループ<code>{}</code>個</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>スーパーグループ<code>{}</code>個</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>チャンネル<code>{}</code>個</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>管理者<code>{}</code>個</b>\n"
        ),
    }

    strings_ua = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>Обробка...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>Ось список найчастіше використовуваних слів у цьому чаті:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>Статистика отримана за <code>{}</code> секунд.</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>У вас <code>{}</code> особистих чатів</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>У вас {} ботів</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Ви в <code>{}</code> групах</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Ви в <code>{}</code> супергрупах</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>Ви в <code>{}</code> каналах</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>Ви адмін в <code>{}</code> чатах </b>\n"
        ),
    }

    strings_kz = {
        "wait": "<emoji id=5325872701032635449>⏳</emoji> <b>Өңдеу...</b>",
        "list": "<emoji id=5963242192741863664>📝</emoji> <b>Осы чатта ең көп қолданылатын сөздер тізімі:</b>\n\n{}",
        "chats": (
            "<emoji id=5467632554813169805>😾</emoji> <b>Статистика <code>{}</code> секунд ішінде алынды.</b>\n\n"
            "<emoji id=5467873721521806850>👤</emoji> <b>Сізде <code>{}</code> жеке чат бар</b>\n"
            "<emoji id=5467884562019261930>🤖</emoji> <b>Сізде {} бот бар</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Сіз <code>{}</code> топта</b>\n"
            "<emoji id=5467772583631921166>👥</emoji> <b>Сіз <code>{}</code> супертопта</b>\n"
            "<emoji id=5467813634929336089>📮</emoji> <b>Сіз <code>{}</code> каналда</b>\n"
            "<emoji id=5467790927437242604>👮</emoji> <b>Сіз <code>{}</code> чатта әкімшісіз </b>\n"
        ),
    }

    @loader.command()
    async def wordcound(self, app: Client, message: types.Message):
        """Discovers the 10 most common words in the latest 1000 messages from a group or private chat."""

        msg_ = await message.answer(self.strings("wait"))

        words = Elevator()

        async for msg in app.get_chat_history(message.chat.id, limit=1000):
            asyncio.sleep(0.1)

            if msg.text:
                for word in msg.text.split():
                    words[word.lower()] += 1

            if msg.caption:
                for word in msg.caption.split():
                    words[word.lower()] += 1

            freq = sorted(words.items(), key=lambda x: x[1], reverse=True)

            out = self.strings("list").format(
                "\n".join(
                    [
                        f"<emoji id=5787589837200562063>⚡️</emoji> <b>{x[0]}</b> - <code>{x[1]}</code>"
                        for x in freq[:10]
                    ]
                )
            )

            await msg_.edit(out)

    @loader.command()
    async def chats(self, app: Client, message: types.Message):
        """Shows stats of your chats"""

        msg_ = await message.answer(self.strings("wait"))

        start = datetime.datetime.now()

        private_chats = 0
        bots = 0
        groups = 0
        supergroups = 0
        channels = 0
        admin = 0

        async for d in app.get_dialogs():
            if d.chat.type == enums.ChatType.PRIVATE:
                private_chats += 1

            elif d.chat.type == enums.ChatType.BOT:
                bots += 1

            elif d.chat.type == enums.ChatType.GROUP:
                groups += 1

            elif d.chat.type == enums.ChatType.SUPERGROUP:
                supergroups += 1

                user_status = await app.get_chat_member(d.chat.id, "me")

                if user_status.status in (
                    enums.ChatMemberStatus.ADMINISTRATOR,
                    enums.ChatMemberStatus.OWNER,
                ):
                    admin += 1

            elif d.chat.type == enums.ChatType.CHANNEL:
                channels += 1

        end = datetime.datetime.now()

        sec = (end - start).seconds

        await msg_.edit(
            self.strings("chats").format(
                sec, private_chats, bots, groups, supergroups, channels, admin
            )
        )
