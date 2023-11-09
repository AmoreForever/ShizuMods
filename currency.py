# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/currencyconverter.jpg?raw=true


import aiohttp
import logging

from .. import loader, utils

from pyrogram import types, Client

logger = logging.getLogger(__name__)


@loader.module("Currency", "hikamoru")
class CurrencyConverter(loader.Module):
    """Extended and faster currency converter, uses: https://currency.hikamoru.uz/"""

    strings = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Processing...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Invalid arguments!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> The <b>{}</b> is:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API is down!</b>\n\nContact @hikamoru for more information.",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>I'm really sorry but you cannot convert TON to currency.</b>",
    }

    strings_ru = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Обработка...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Неверные аргументы!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{}</b> равен:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API не работает!</b>\n\nСвяжитесь с @hikamoru для получения дополнительной информации.",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>Мне очень жаль, но вы не можете конвертировать TON в валюту.</b>,,,"
    }

    strings_uz = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Kuting...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Noto'g'ri argumentlar!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{}</b> teng:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API ishlamayapti!</b>\n\nQo'shimcha ma'lumot uchun @hikamoru bilan bog'laning.",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>Uzr, lekin siz TONni valyutaga aylantira olmaysiz.</b>,,,"
    }

    strings_jp = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>処理中...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>無効な引数！</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{}</b> は:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API がダウンしています！</b>\n\n詳細については、@hikamoru にお問い合わせください。",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>申し訳ありませんが、TONを通貨に変換することはできません。</b>,,,"
    }

    strings_ua = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Обробка...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Невірні аргументи!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{}</b> дорівнює:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API не працює!</b>\n\nЗв'яжіться з @hikamoru для отримання додаткової інформації.",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>Вибачте, але ви не можете конвертувати TON в валюту.</b>,,,"
    }

    strings_kz = {
        "processings": "<emoji id=5267468588985363056>⏳</emoji> <b>Өңдеу...</b>",
        "args": "<emoji id=5017122105011995219>⛔️</emoji> <b>Қате аргументтер!</b>",
        "result": "<emoji id=5370874247373660919>💸</emoji> <b>{}</b> тең:\n\n{}",
        "api_down": "<emoji id=5819177212833697095>🪫</emoji> <b>API жұмыс істемейді!</b>\n\nТолық ақпарат алу үшін @hikamoru-мен байланысыңыз.",
        "cannot_convert_ton": "<emoji id=5819177212833697095>🪫</emoji> <b>Кешіріңіз, бірақ сіз TON-ді валютага айналдыра алмайсыз.</b>,,,"
    }

    def __init__(self):
        self.api = "https://currency.hikamoru.uz/convert/"

    async def formulate_request(self, amount, currency):
        """
        Executes the currency conversion request and returns the formatted result.

        :param amount: The amount to convert.
        :param currency: The currency to convert to.

        return: The formatted result of the currency conversion.

        """

        params = {"amount": amount, "currency": currency}
        user_agent = {"User-Agent": "Shizu-Userbot"}

        async with aiohttp.ClientSession() as session:
            response = await session.get(self.api, params=params, headers=user_agent)
            json = await response.json()

        return "\n".join(
            f"{utils.get_lang_flag(currency[:2])} {currency.upper()}: <code>{value.split('.')[0]}</code>"
            for currency, value in json["data"].items() - {"ton"}
        )

    @loader.command()
    async def conv(self, app: Client, message: types.Message):
        """Converts the specified currency with the specified amount to all currencies. Usage: .conv (amount) (currency)"""

        args = utils.get_args(message).split()

        amount, currency = args

        if len(currency) != 3:
            await utils.answer(message, self.strings("args"))
            return

        if currency.lower() == "ton":
            await utils.answer(message, self.strings("cannot_convert_ton"))
            return

        if not amount.isdigit():
            await utils.answer(message, self.strings("args"))
            return

        await utils.answer(message, self.strings("processings"))

        try:
            result = await self.formulate_request(amount, currency)
        except Exception as error:
            logging.error(error)
            await utils.answer(message, self.strings("api_down"))
            return

        await utils.answer(
            message, self.strings("result").format(f"{amount} {currency}", result)
        )
