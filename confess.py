# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/confess.jpg?raw=true


import string
import logging
import random
import asyncio

from pyrogram.types import Message
from pyrogram import enums

from .. import loader

logger = logging.getLogger(__name__)


@loader.module("Confess", "hikamoru", 1)
class Confess(loader.Module):
    """If expressing your love feels too modest for you, use this module to confess your love to someone."""

    strings = {
        "sympathy": [
            "👋 <i>Hello. I'm <b>Shizu</b></i>",
            "🫣 <i>My owner is too humble to express himself, so he requested my assistance...</i>",
            "😊 <i>He simply wanted to convey that <b>he holds affection for you</b>...</i>",
            "🤗 <i>These feelings are sincere... Please, understand and don't hold it against him.</i>",
            "🌟 <i>It would mean a lot to him if you could share some kind words... 😊</i>",
            "💬 <i>Feel free to respond with your thoughts or feelings!</i>",
            "📧 <i>You can also reach out to him directly if you wish to chat more.</i>",
        ],
        "message": "<emoji id=5787148752649195233>💌</emoji> <i>Hey pretty, you have one unread message click <a href='{}'>here to read</a></i>",
        "only_private": "<emoji id=5456581719924678628>😳</emoji> This command can only be used in private chats.",
        "dm_button": "💗 DM",
        "nla": "🙄 <b>No longer available</b>",
        "readed": "📩 <i>Your confess has been read by {}</i>",
    }

    strings_ru = {
        "sympathy": [
            "👋 <i>Привет. Я - <b>Шизу</b></i>",
            "🫣 <i>Мой владелец слишком застенчив, чтобы выразить свои чувства, поэтому он попросил меня помочь...</i>",
            "😊 <i>Он просто хочет, чтобы вы знали, что <b>он в вас влюблен</b>...</i>",
            "🤗 <i>Эти чувства искренни... Пожалуйста, будьте понимающими и не обижайтесь на него.</i>",
            "🌟 <i>Ему будет приятно, если вы выскажете ему добрые слова... 😊</i>",
            "💬 <i>Не стесняйтесь выразить свои мысли или чувства!</i>",
            "📧 <i>Вы также можете напрямую связаться с ним, если хотите поболтать больше.</i>",
        ],
        "message": "<emoji id=5787148752649195233>💌</emoji> <i>Привет красивая, у тебя есть одно непрочитанное сообщение, <a href='{}'>нажми сюда что-бы прочитать</a></i>",
        "only_private": "<emoji id=5456581719924678628>😳</emoji> Эта команда может использоваться только в личных чатах.",
        "dm_button": "💗 ЛС",
        "nla": "🙄 <b>Больше недоступно</b>",
        "readed": "📩 <i>Ваше признание было прочитано {}</i>",
    }

    strings_kr = {
        "sympathy": [
            "👋 <i>안녕하세요. 저는 <b>시즈</b>입니다.</i>",
            "🫣 <i>주인님은 자신의 감정을 표현하는 것이 너무 겸손해서 제 도움을 요청했습니다...</i>",
            "😊 <i>그는 단지 <b>당신을 사랑한다는 것을 전하고 싶어합니다</b>...</i>",
            "🤗 <i>이 감정은 진실입니다... 이해해주시고 그를 원망하지 마십시오.</i>",
            "🌟 <i>당신이 친절한 말을 나눠주신다면 그에게 많은 의미가 있을 것입니다... 😊</i>",
            "💬 <i>자신의 생각이나 감정을 자유롭게 표현해보세요!</i>",
            "📧 <i>더 이야기하고 싶다면 직접 연락을 취할 수도 있습니다.</i>",
        ],
        "message": "<emoji id=5787148752649195233>💌</emoji> <i>안녕 예쁜이, 당신에게 하나의 읽지 않은 메시지가 있습니다, <a href='{}'>여기를 클릭하여 읽으십시오</a></i>",
        "only_private": "<emoji id=5456581719924678628>😳</emoji> 이 명령은 개인 채팅에서만 사용할 수 있습니다.",
        "dm_button": "💗 DM",
        "nla": "🙄 <b>더 이상 사용할 수 없습니다</b>",
        "readed": "📩 <i>당신의 고백은 {}에 읽혔습니다</i>",
    }

    @loader.command()
    async def confess(self, app, message: Message):
        """<b>Confess your love to someone</b>\n\nUse this command to confess your love to someone. Just type the command and I will do the rest for you."""
        if message.chat.type == enums.ChatType.PRIVATE:
            random_id = "".join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )

            ids = self.db.get("confess", "ids", {})
            ids[random_id] = message.chat.id
            self.db.set("confess", "ids", ids)

            await message.answer(
                self.strings("message").format(
                    (
                        "https://t.me/"
                        + (await self.bot.bot.get_me()).username
                        + "?start=lav_"
                        + random_id
                    )
                )
            )

        else:
            await message.answer(self.strings("only_private"))

    @loader.on_bot(lambda self, app, m: m.chat.type == "private")
    async def confess_message_handler(self, app, message):

        if message.text and message.text.startswith("/start lav_"):

            random_id = message.text.split("_", 1)[1]
            ids = self.db.get("confess", "ids", {})
            markup = self.bot._generate_markup(
                [
                    [
                        {
                            "text": self.strings("dm_button"),
                            "url": f"tg://user?id={self.tg_id}",
                        }
                    ]
                ]
            )

            if random_id in ids:

                self.db.pop("confess", "ids", random_id)

                for i in range(len(self.strings("sympathy")) - 1):
                    await asyncio.sleep(3)
                    await self.bot.bot.send_message(
                        message.chat.id, self.strings("sympathy")[i]
                    )

                await self.bot.bot.send_message(
                    message.chat.id, self.strings("sympathy")[-1], reply_markup=markup
                )

                await self.bot.bot.send_message(
                    self.tg_id, self.strings("readed").format(message.chat.mention)
                )

            else:
                await self.bot.bot.send_message(message.chat.id, self.strings("nla"))
