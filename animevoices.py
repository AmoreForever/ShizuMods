# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/animevoices.jpg?raw=true

from .. import loader


@loader.module("AnimeVoices", "shizumods")
class AnimeVoicesMod(loader.Module):
    """🎤 Popular Anime Voices"""

    async def smexkcmd(self, app, message):
        """Смех Канеки"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/27",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def smexycmd(self, app, message):
        """Смех Ягами"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/28",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def znaycmd(self, app, message):
        """Знай свое место ничтожество"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/29",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def madaraccmd(self, app, message):
        """Учиха Мадара"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/30",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def sharingancmd(self, app, message):
        """Итачи Шаринган"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/30",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def imsasukecmd(self, app, message):
        """Учиха Саске"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/32",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def paincmd(self, app, message):
        """Познайте боль"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/6",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def rascmd(self, app, message):
        """Расширение территории"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/8",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def tenseicmd(self, app, message):
        """Shinra tensei"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/9",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def dazaicmd(self, app, message):
        """Дазаи"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/10",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def gaycmd(self, app, message):
        """I'm gay"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/11",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def bankaicmd(self, app, message):
        """Bankai"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/12",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def satecmd(self, app, message):
        """Sate sate sate"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/13",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def yoaimocmd(self, app, message):
        """Yoaimo"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/14",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def madaracmd(self, app, message):
        """Он один из основателей конохи"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/15",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def valhallacmd(self, app, message):
        """У нас будет крутейшая байкерская банда в Канто."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/16",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def itachicmd(self, app, message):
        """В возрасте 7 лет он уже мыслил как Хокаге."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/17",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def ghoulcmd(self, app, message):
        """Я...Гуль."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/18",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def bestcmd(self, app, message):
        """В общем раз уж я сдесь стану лучшим.(Повар боец Сомо)"""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/19",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def requiemcmd(self, app, message):
        """Это реквием."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/20",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def kingcmd(self, app, message):
        """Король вернулся."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/21",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def equalitycmd(self, app, message):
        """цитата Аянокоджи про равенство."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/22",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def forestcmd(self, app, message):
        """Нельзя понять всю красоту леса оценивая лишь одно дерево."""

        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/23",
            reply_to_message_id=reply.id if reply else None,
        )
        return

    async def bankaiichigocmd(self, app, message):
        """Банкай Ичиго."""
        reply = message.reply_to_message
        await message.delete()
        await app.send_document(
            message.chat.id,
            "https://t.me/AniVoicec/24",
            reply_to_message_id=reply.id if reply else None,
        )
        return
