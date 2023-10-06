# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# required: Pillow

# banner: https://github.com/AmoreForever/shizuassets/blob/master/hacker.jpg?raw=true

from .. import loader, utils
import requests
from PIL import Image, ImageFont, ImageDraw
import io
from textwrap import wrap


@loader.module("Hacker", "hikamoru")
class HackerMod(loader.Module):
    """Create hacker message stickers"""

    strings = {
        "what": 'Reply to text or write text <emoji id="5467928559664242360">❗️</emoji>',
        "processing": 'Processing <emoji id="6334710044407368265">🚀</emoji>',
    }

    @loader.command()
    async def hackercmd(self, app, message):
        """Reply to text or write text"""

        ufr = requests.get(
            "https://github.com/AmoreForever/assets/raw/master/CryptoCrashItalic-vmogL.ttf"
        )
        f = ufr.content

        reply = message.reply_to_message
        if args := utils.get_args_raw(message):
            txt = utils.get_args_raw(message)
        elif reply:
            txt = reply.text or reply.caption
        else:
            await message.answer(self.strings["what"])
            return
        await message.answer(self.strings["processing"])
        pic = requests.get(
            "https://github.com/AmoreForever/assets/blob/master/photo_2023-10-02_12-38-35.jpg?raw=true"
        )
        pic.raw.decode_content = True
        img = Image.open(io.BytesIO(pic.content)).convert("RGB")

        W, H = img.size
        txt = txt.replace("\n", "𓃐")
        text = "\n".join(wrap(txt, 19))
        t = text + "\n"
        t = t.replace("𓃐", " \n")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(io.BytesIO(f), 32, encoding="UTF-8")
        w, h = draw.multiline_textsize(t, font=font)
        imtext = Image.new("RGBA", (w + 10, h + 10), (255, 250, 250, 1))
        draw = ImageDraw.Draw(imtext)
        draw.multiline_text((10, 10), t, (255, 255, 255), font=font, align="left")
        imtext.thumbnail((339, 181))
        w, h = 339, 181
        img.paste(imtext, (10, 10), imtext)
        out = io.BytesIO()
        out.name = "amore.webp"
        img.save(out)
        out.seek(0)
        await message.answer(
            out, doc=True, reply_to_message_id=reply.id if reply else None
        )
