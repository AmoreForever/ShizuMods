# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/lymusic.jpg?raw=true

from pyrogram.types import Document
from pyrogram import Client

from .. import loader, utils


@loader.module("LyMusic", "shizumods")
class LyMusic(loader.Module):
    """Music search"""

    strings = {
        "searching": "<emoji id=5316919120149619748>🎧</emoji> Searching for you <3 ",
        "no_args": "<b>Provide arguments or reply to a message!</b>",
        "cannot": "<emoji id=5228855428540013962>🙈</emoji> <b>Sorry, I can't find this song.</b>",
        "caption": "<emoji id=5316919120149619748>🎧</emoji> <b>Here it is <u>{}</u></b>",
    }
    strings_ru = {
        "searching": "<emoji id=5316919120149619748>🎧</emoji> Ищу для тебя <3",
        "no_args": "<b>Укажите аргументы или ответьте на сообщение!</b>",
        "cannot": "<emoji id=5228855428540013962>🙈</emoji> <b>Извини, я не смог найти эту песню.</b>",
        "caption": "<emoji id=5316919120149619748>🎧</emoji> <b>Вот она <u>{}</u></b>",
    }
    strings_uz = {
        "searching": "<emoji id=5316919120149619748>🎧</emoji> Siz uchun qidiryapman <3 ",
        "no_args": "<b>Argumentlarni ko'rsating yoki habarga javob bering!</b>",
        "cannot": "<emoji id=5228855428540013962>🙈</emoji> <b>Uzr, bu qo'shiqni topolmadim.</b>",
        "caption": "<emoji id=5316919120149619748>🎧</emoji> <b>Mana <u>{}</u></b>",
    }
    strings_jp = {
        "searching": "<emoji id=5316919120149619748>🎧</emoji> あなたのために探しています <3 ",
        "no_args": "<b>引数を指定するか、メッセージに返信してください！</b>",
        "cannot": "<emoji id=5228855428540013962>🙈</emoji> <b>すみません、この曲が見つかりません。</b>",
        "caption": "<emoji id=5316919120149619748>🎧</emoji> <b>ここに <u>{}</u></b>",
    }

    @loader.command()
    async def lym(self, app: Client, message):
        """Search music - args or reply to a message"""
        args = utils.get_args_raw(message)
        reply = message.reply_to_message
        if not args and not reply:
            return await message.answer(self.strings("no_args"))
        query = args or reply.text
        await message.answer(self.strings("searching"))
        try:
            result = (
                (await app.get_inline_bot_results("@lybot", f"{query}"))
                .results[0]
                .document
            )
        except Exception:
            return await message.answer(self.strings("cannot"))
        lyrics = Document._parse(
            client=app,
            document=result,
            file_name="test",
        )
        await message.delete()
        await app.send_document(
            message.chat.id,
            lyrics.file_id,
            caption=self.strings("caption").format(result.attributes[1].file_name),
            reply_to_message_id=reply.id if reply else None,
        )
