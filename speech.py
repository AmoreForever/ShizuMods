# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# requires: pydub speechrecognition python-ffmpeg

import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from .. import loader, utils

logger = logging.getLogger(__name__)
recognizer = sr.Recognizer()


@loader.module("Speech", "hikamoru")
class SpeechMod(loader.Module):
    """Speech Recognition"""

    strings = {
        "only_voice": "<emoji id=5877477244938489129>🚫</emoji> <b>Reply to a voice message!</b>",
        "downloading": "<emoji id=5213251580425414358>🔽</emoji> <b>Downloading...</b>",
        "recognizing": "<emoji id=5472199711366584503>👂</emoji> <b>Recognizing...</b>",
        "not_recognized": "<emoji id=5877477244938489129>🚫</emoji> <b>Not recognized</b>",
        "request_error": "<emoji id=5877477244938489129>🚫</emoji> <b>Request error occured.\n{}</b>",
        "recognized": "<emoji id=5267468588985363056>🚛</emoji> <b>Recognized:</b> <code>{}</code>",
        "language_set": "<emoji id=5267468588985363056>🚛</emoji> <b>Language set to {}</b>",
    }

    def __init__(self):
        self.config = {"language": self.db.get("speech", "language", None) or "ru"}

    @loader.command()
    async def setspechlg(self, app, message):
        """Set recognition language"""
        self.config["language"] = message.get_args_raw()
        self.db.set("speech", "language", self.config["language"])
        logger.info("[speech] Language set to %s", self.config["language"])
        await utils.answer(
            message, self.strings["language_set"].format(self.config["language"])
        )

    @loader.command()
    async def speech(self, app, message):
        """Use .speech [reply to voice]"""
        reply = message.reply_to_message
        if not reply or not reply.voice:
            await utils.answer(message, self.strings["only_voice"])
            return
        await utils.answer(message, self.strings["downloading"])
        voice = await app.download_media(reply.voice)
        wav_voice = voice.replace(voice.split(".")[-1], "wav")
        ogg_audio = AudioSegment.from_ogg(voice)
        ogg_audio.export(wav_voice, format="wav")
        audio = sr.AudioFile(wav_voice)
        with audio as source:
            try:
                audio = recognizer.record(source)
                await utils.answer(message, self.strings["recognizing"])
                recognized = recognizer.recognize_google(
                    audio, language=self.config["language"]
                )
            except sr.UnknownValueError:
                await utils.answer(message, self.strings["not_recognized"])
                return
            except sr.RequestError as e:
                await utils.answer(message, self.strings["request_error"].format(e))
                return
        await utils.answer(message, self.strings["recognized"].format(recognized))
        os.remove(voice)
        os.remove(wav_voice)
