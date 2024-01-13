# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/currencyconverter.jpg?raw=true

import requests
import aiohttp

from pyrogram import Client, types

from .. import loader, utils


@loader.module("Currency", "shizumods", 1.1)
class CurrencyConverter(loader.Module):
    """Extended and faster currency converter, uses: https://app.exchangerate-api.com/"""

    strings = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Processing...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Invalid arguments!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> The <b>{} {}</b> is:\n\n{}",
    }

    strings_ru = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Обработка...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Неверные аргументы!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{} {}</b> это:\n\n{}",
    }


    async def convert_currency(self, amount, from_currency):
        base_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        async with aiohttp.ClientSession() as session:
            async with session.get(base_url) as response:
                data = await response.json()

        return [
            f"<b>{utils.get_lang_flag(''.join(i[:2]))} {i}</b>: <code>{data['rates'][i] * float(amount)}</code>"
            for i in data["rates"]
        ]

    @loader.command()
    async def conv(self, app: Client, message: types.Message):
        """Converts the specified currency with the specified amount to all currencies. Usage: .conv (amount) (currency)"""

        args = message.get_args().split()

        if len(args) != 2:
            await utils.answer(message, self.strings("args"))
            return

        m = await utils.answer(message, self.strings("processings"))

        amount, currency = args[0], args[1].upper()

        result = await self.convert_currency(amount, currency)

        await utils.answer(
            m, self.strings("result").format(amount, currency, "\n".join(result))
        )
