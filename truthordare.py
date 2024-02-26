# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/truthordare.jpg?raw=true


# requires: deep-translator requests

import random
import requests
import deep_translator

from pyrogram import types, Client
from aiogram.types import CallbackQuery

from .. import loader


@loader.module("Truth or Dare", "shizumods", 1.0)
class Truthordare(loader.Module):
    """Play Truth or Dare in Telegram! Choose 'truth' for personal questions or 'dare' for fun challenges – all in one compact module!"""

    strings = {
        "truth": "🕵️‍♂️ Truth",
        "dare": "🔥 Dare",
        "format": ("🙆 <b>Step:</b> {}\n\n" "📜 <b>Question:</b> {}\n"),
        "choose_level": "📊 Choose a level:",
        "choose_language": "🏮 Choose a language:",
        "levels": [
            "👦 Simple",
            "👦 Simple [advanced]",
            "🧘‍♂️ Medium",
            "🍓 Hot",
            "🔞 Hot [advanced]",
        ],
    }

    strings_ru = {
        "truth": "🕵️‍♂️ Правда",
        "dare": "🔥 Действие",
        "format": ("🙆 <b>Очередь:</b> {}\n\n" "📜 <b>Вопрос:</b> {}\n"),
        "choose_level": "📊 Выберите уровень:",
        "choose_language": "🏮 Выберите язык:",
        "levels": [
            "👦 Простой",
            "👦 Простой [продвинутый]",
            "🧘‍♂️ Средний",
            "🍓 Горячий",
            "🔞 Горячий [продвинутый]",
        ],
    }

    async def _generate_question(
        self, question_type: str, level: str, language: str
    ) -> str:
        data = requests.get(
            "https://gist.githubusercontent.com/AmoreForever/ee3de42507474afc166f22f5c8e7d915/raw/a4eabde445bb74ef0303db6a8589fcd7363e220f/truth_or_dare.json"
        ).json()

        filtered_questions = [
            q for q in data if q["level"] == level and q["type"] == question_type
        ]

        if not filtered_questions:
            return "No matching question found."

        question = random.choice(filtered_questions)

        if language != "en":
            return deep_translator.GoogleTranslator(
                source="auto", target=language
            ).translate(question["summary"])

        return question["summary"]

    async def tod_question_callback_(
        self, call: CallbackQuery, question_type: str, level: str, language: str
    ):
        await call.answer()

        buttons = [
            [
                {
                    "text": self.strings("truth"),
                    "callback": self.tod_question_callback_,
                    "args": (
                        "Truth",
                        level,
                        language,
                    ),
                },
                {
                    "text": self.strings("dare"),
                    "callback": self.tod_question_callback_,
                    "args": (
                        "Dare",
                        level,
                        language,
                    ),
                },
            ]
        ]

        await call.edit(
            self.strings("format").format(
                call.from_user.full_name,
                await self._generate_question(question_type, level, language),
            ),
            reply_markup=buttons,
            force_me=False,
        )

    async def _choose_level_callback_(self, call, language):
        levels = {
            1: self.strings("levels")[0],
            2: self.strings("levels")[1],
            3: self.strings("levels")[2],
            4: self.strings("levels")[3],
            5: self.strings("levels")[4],
        }

        buttons = []
        for i, level in levels.items():
            button = {
                "text": level,
                "callback": self.tod_question_callback_,
                "args": ("Truth", str(i), language),
            }
            buttons.append([button])

        await call.edit(
            self.strings("choose_level"),
            reply_markup=buttons,
            force_me=False,
        )

    @loader.command()
    async def tod(self, app: Client, message: types.Message):
        """Start new game of Truth or Dare."""

        buttons = [
            [
                {
                    "text": "🇬🇧 English",
                    "callback": self._choose_level_callback_,
                    "args": ("en",),
                },
                {
                    "text": "🇷🇺 Русский (может быть кривой перевод)",
                    "callback": self._choose_level_callback_,
                    "args": ("ru",),
                },
            ]
        ]

        await message.answer(
            self.strings("choose_language"),
            reply_markup=buttons,
            force_me=False,
        )
