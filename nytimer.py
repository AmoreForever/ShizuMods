# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

from .. import loader, utils
import datetime
from time import strftime


@loader.module("NYMod", "hikamoru")
class NYMod(loader.Module):
    """Check how much is left until the new year"""

    async def nycmd(self, app, message):
        """Check date"""
        now = datetime.datetime.today()
        ng = datetime.datetime(int(strftime("%Y")) + 1, 1, 1)
        d = ng - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        soon = "<b><emoji id=6334530007968253960>☃️</emoji> Until the <u>New Year</u>: {} d. {} h. {} m. {} s.</b>\n<b><emoji id=5393226077520798225>🥰</emoji> Celebrate the new year together <u>Shizu</u></b>".format(
            d.days, hh, mm, ss
        )
        await message.answer(soon)
