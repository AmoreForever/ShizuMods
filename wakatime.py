# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


# required: aiohttp
# banner: https://github.com/AmoreForever/shizuassets/blob/master/wakatime.jpg?raw=true


import asyncio
import aiohttp

from pyrogram import types, Client
from .. import utils, loader


@loader.module("Wakatime", "hikamoru", 1.0)
class Wakatime(loader.Module):
    """Show your Wakatime stats"""

    strings = {
        "set_waka": "Set your Wakatime token",
        "no_token": "🚫 <b>You don't have a token</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "WAKATIME_TOKEN",
            None,
            lambda: self.strings["set_waka"],
        )

    @loader.command()
    async def waka(self, app: Client, message: types.Message):
        """See your stat"""
        token = self.config["WAKATIME_TOKEN"]
        if token is None:
            return await message.answer(self.strings("no_token"))
        async with aiohttp.ClientSession() as session:
            tasks = [
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/status_bar/today?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/stats/all_time?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/stats/all_time?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/all_time_since_today?api_key={token}",
                ),
            ]
            result_t, result, result_s, result_w = await asyncio.gather(*tasks)
            result_t = await result_t.json()
            result = await result.json()
            result_s = await result_s.json()
            result_w = await result_w.json()

            all_time = result_w["data"]["text"]
            username = result["data"]["username"]
            languages = result["data"]["languages"]
            today = result_t["data"]["categories"]
            os = result["data"]["operating_systems"]
            OS = ", ".join(
                [
                    f"<code>{stat['name']}</code>"
                    for stat in os
                    if stat["text"] != "0 secs"
                ]
            )
            editor = result["data"]["editors"]
            EDITOR = ", ".join(
                [
                    f"<code>{stat['name']}</code> "
                    for stat in editor
                    if stat["text"] != "0 secs"
                ]
            )
            LANG = "\n".join(
                [
                    f"▫️ <b>{stat['name']}</b>: <i>{stat['text']}</i>"
                    for stat in languages
                    if stat["text"] != "0 secs"
                ]
            )
            TODAY = "\n".join(
                [f"{stat['text']}" for stat in today if stat["text"] != "0 secs"]
            )
            await message.answer(
                f"👤 <b>Username:</b> <code>{username}</code>\n🖥 <b>OS:</b> {OS}\n🌀 <b>Editor:</b> {EDITOR}\n⏳ <b>All time</b>: <code>{all_time}</code>\n💼 <b>Today</b>: <code>{TODAY}</code>\n\n🧬 LANGUAGES\n\n{LANG}\n",
                reply_markup=[
                    [
                        {
                            "text": "🔄 Update",
                            "callback": self.update_waka,
                        }
                    ]
                ],
            )

    async def update_waka(self, call):
        await call.edit("🔄 <b>Updating...</b>")
        token = self.config["WAKATIME_TOKEN"]
        if token is None:
            return await call.edit(self.strings("no_token"))
        async with aiohttp.ClientSession() as session:
            tasks = [
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/status_bar/today?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/stats/all_time?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/stats/all_time?api_key={token}",
                ),
                session.request(
                    "GET",
                    f"https://wakatime.com/api/v1/users/current/all_time_since_today?api_key={token}",
                ),
            ]
            result_t, result, result_s, result_w = await asyncio.gather(*tasks)
            result_t = await result_t.json()
            result = await result.json()
            result_s = await result_s.json()
            result_w = await result_w.json()

            all_time = result_w["data"]["text"]
            username = result["data"]["username"]
            languages = result["data"]["languages"]
            today = result_t["data"]["categories"]
            os = result["data"]["operating_systems"]
            OS = ", ".join(
                [
                    f"<code>{stat['name']}</code>"
                    for stat in os
                    if stat["text"] != "0 secs"
                ]
            )
            editor = result["data"]["editors"]
            EDITOR = ", ".join(
                [
                    f"<code>{stat['name']}</code> "
                    for stat in editor
                    if stat["text"] != "0 secs"
                ]
            )
            LANG = "\n".join(
                [
                    f"▫️ <b>{stat['name']}</b>: <i>{stat['text']}</i>"
                    for stat in languages
                    if stat["text"] != "0 secs"
                ]
            )
            TODAY = "\n".join(
                [f"{stat['text']}" for stat in today if stat["text"] != "0 secs"]
            )
            await call.edit(
                f"👤 <b>Username:</b> <code>{username}</code>\n🖥 <b>OS:</b> {OS}\n🌀 <b>Editor:</b> {EDITOR}\n⏳ <b>All time</b>: <code>{all_time}</code>\n💼 <b>Today</b>: <code>{TODAY}</code>\n\n🧬 LANGUAGES\n\n{LANG}\n",
            )
