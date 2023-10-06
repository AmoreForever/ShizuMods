# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


# required: phlogo
# banner: https://github.com/AmoreForever/shizuassets/blob/master/phsticker.jpg?raw=true

import os
from .. import loader, utils
from phlogo import generate


@loader.module("Phlogo", "hikamoru")
class PhLogo(loader.Module):
    """Make Pornhub logo sticker"""

    strings = {
        "only_two": "<emoji id=5242451340789030607>🙅‍♀️</emoji>  <b>Something's wrong. Try giving two words only like <code>Hello world</code></b>",
        "none_args": "<emoji id=5350635554021061942>🥹</emoji> <b>Give some text bruh, e.g.</b>: <code>Hello world</code>",
    }

    @loader.command()
    async def phl(self, app, message):
        "makes Pornhub style logo sticker. only 2 words"
        args = utils.get_args_raw(message).split(" ")
        reply = message.reply_to_message
        if args == " ":
            await utils.answer(message, self.strings["none_args"])
            return
        try:
            p = args[0]
            h = args[1]
        except Exception:
            await utils.answer(message, self.strings["only_two"])
            return
        result = generate(f"{p}", f"{h}")
        result.save("ph.webp")
        path = os.getcwd()
        stc = f"{path}/ph.webp"
        await message.delete()
        await message.answer(
            stc,
            doc=True,
            caption=f"{p} {h}",
        )
        os.remove(stc)
