# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# required: groq


import logging
import requests
from typing import Optional

from datetime import datetime

from groq import Groq
from groq.types.chat import ChatCompletion

from .. import loader, utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@loader.module("FreeGPT", "shizumods")
class FreeGPT(loader.Module):
    """Advanced Free Alternative to ChatGPT with Enhanced Features"""

    strings = {
        "no_input": "❗ Reply to a message or provide text input",
        "no_token": "🚫 GROQ API token not configured. Please set it in module config.",
        "processing": "🚀 Processing your request...",
        "error": "⚠️ An error occurred: {error}",
        "response": (
            "<emoji id='5325695795624682172'>🐱</emoji> <b>Your Question:</b> <code>{question}</code>\n\n"
            "<emoji id='5359726582447487916'>📱</emoji> <b>Answer:</b> {answer}\n\n"
            "<emoji id='5947553854030614234'>📊</emoji> Tokens Used: <code>{tokens}</code> | Model: <code>{model}</code>"
        ),
        "_cfg_doc_groq_token": "Your GROQ API token from https://console.groq.com/keys",
        "_cfg_doc_default_model": "Default AI model to use",
        "_cfg_doc_max_tokens": "Maximum tokens for response",
        "_cfg_doc_temperature": "Creativity/randomness of response",
    }

    strings_ru = {
        "no_input": "❗ Ответьте на сообщение или укажите текст",
        "no_token": "🚫 Токен GROQ API не настроен. Пожалуйста, укажите его в конфигурации модуля.",
        "processing": "🚀 Обрабатываю ваш запрос...",
        "error": "⚠️ Произошла ошибка: {error}",
        "response": (
            "<emoji id='5325695795624682172'>🐱</emoji> <b>Ваш вопрос:</b> <code>{question}</code>\n\n"
            "<emoji id='5359726582447487916'>📱</emoji> <b>Ответ:</b> {answer}\n\n"
            "<emoji id='5947553854030614234'>📊</emoji> Использовано токенов: <code>{tokens}</code> | Модель: <code>{model}</code>"
        ),
        "_cfg_doc_groq_token": "Ваш токен GROQ API с https://console.groq.com/keys",
        "_cfg_doc_default_model": "Модель ИИ по умолчанию для использования",
        "_cfg_doc_max_tokens": "Максимальное количество токенов для ответа",
        "_cfg_doc_temperature": "Креативность/случайность ответа",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "groq_token",
            None,
            lambda: self.strings["_cfg_doc_groq_token"],
            "default_model",
            "llama3-8b-8192",
            lambda: self.strings["_cfg_doc_default_model"],
            "max_tokens",
            2048,
            lambda: self.strings["_cfg_doc_max_tokens"],
            "temperature",
            0.7,
            lambda: self.strings["_cfg_doc_temperature"],
        )
        self._client = None

    def _init_client(self):
        """Initialize Groq client if not already initialized"""
        if not self._client and self.config["groq_token"]:
            self._client = Groq(api_key=self.config["groq_token"])
        return self._client

    @loader.command()
    async def fgpt_models(self, app, message):
        url = "https://api.groq.com/openai/v1/models"
        headers = {
            "Authorization": f"Bearer {self.config['groq_token']}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            models = response.json().get("data", [])

            grouped_models = {}
            for model in models:
                owner = model.get("owned_by", "Unknown")
                if owner not in grouped_models:
                    grouped_models[owner] = []
                grouped_models[owner].append(model)

            model_details = []
            for owner, owner_models in sorted(grouped_models.items()):
                model_details.append(f"🏢 {owner}:")
                for model in sorted(owner_models, key=lambda x: x["id"]):
                    model_info = (
                        f"  🔹 {model['id']}\n"
                        f"    • Context Window: {model.get('context_window', 'N/A')} tokens\n"
                        f"    • Status: {'🟢 Active' if model.get('active', False) else '🔴 Inactive'}\n"
                        f"    • Created: {datetime.fromtimestamp(model.get('created', 0)).strftime('%Y-%m-%d')}"
                    )
                    model_details.append(model_info)
                model_details.append("")

            response_text = "\n".join(model_details).strip()

            max_message_length = 4096
            if len(response_text) > max_message_length:
                chunks = [
                    response_text[i : i + max_message_length]
                    for i in range(0, len(response_text), max_message_length)
                ]
                for chunk in chunks:
                    await message.reply(chunk)
            else:
                await message.reply(response_text)

        except Exception as e:
            logger.error(f"Error in fgpt_models command: {e}")
            await message.reply(self.strings["error"].format(error=str(e)))

    @loader.command()
    async def fgpt(self, app, message):
        """Process user's text input or replied message"""
        try:
            txt = await self._extract_text(message)
            if not txt:
                await message.reply(self.strings["no_input"])
                return

            if not self.config["groq_token"]:
                await message.reply(self.strings["no_token"])
                return

            processing_msg = await message.answer(self.strings["processing"])

            response = await self._generate_response(txt)

            await processing_msg.edit(
                self.strings["response"].format(
                    question=txt,
                    answer=response.choices[0].message.content,
                    tokens=response.usage.total_tokens,
                    model=response.model,
                )
            )

        except Exception as e:
            logger.error(f"Error in fgpt command: {e}")
            await message.reply(self.strings["error"].format(error=str(e)))

    async def _extract_text(self, message) -> Optional[str]:
        """Extract text from message or reply"""
        if args := utils.get_args_raw(message):
            return args

        reply = message.reply_to_message
        return reply.text or reply.caption if reply else None

    async def _generate_response(self, prompt: str) -> ChatCompletion:
        """Generate AI response with configurable parameters"""
        client = self._init_client()

        return client.chat.completions.create(
            model=self.config["default_model"],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
        )
