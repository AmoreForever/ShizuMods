# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# banner: https://github.com/AmoreForever/shizuassets/blob/master/universaltime.jpg?raw=true

from .. import loader, utils
import datetime

import logging

logger = logging.getLogger(__name__)


def check_time():
    offsets = [3, 5, 4, 2, 1, -7, 6, 9, 5.30, 9, 8, -8, -4]
    hrs = []
    for x in offsets:
        offset = datetime.timedelta(hours=x)
        not_tz = datetime.timezone(offset)
        time = datetime.datetime.now(not_tz)
        format_ = time.strftime("%d.%m.%y | %H:%M")
        hrs.append(format_)
    return f"<emoji id=4920662486778119009>🌐</emoji> <b>Universal time</b>\n\n<emoji id=6323139226418284334>🇷🇺</emoji> Russia ➪ {hrs[0]}\n<emoji id=6323430017179059570>🇺🇿</emoji> Uzbekistan ➪ {hrs[1]}\n<emoji id=6323289850921354919>🇺🇦</emoji> Ukraine ➪ {hrs[3]}\n<emoji id=6323575251498174463>🇦🇿</emoji> Azerbaijan ➪ {hrs[2]}\n<emoji id=6320817337033295141>🇩🇪</emoji> German ➪ {hrs[3]}\n<emoji id=6323589145717376403>🇬🇧</emoji> UK ➪ {hrs[4]}\n<emoji id=6323602387101550101>🇵🇱</emoji> Poland ➪ {hrs[3]}\n<emoji id=6323374027985389586>🇺🇸</emoji> USA ➪ {hrs[5]}\n<emoji id=6323615997852910673>🇰🇬</emoji> Kyrgyzstan ➪ {hrs[6]}\n<emoji id=6323135275048371614>🇰🇿</emoji> Kazakhstan ➪ {hrs[6]}\n<emoji id=6323555846835930376>🇮🇶</emoji> Iraq ➪ {hrs[0]}\n<emoji id=6323356796576597627>🇯🇵</emoji> Japan ➪ {hrs[7]}\n<emoji id=6323152716910561397>🇰🇷</emoji> South KR ➪ {hrs[7]}\n<emoji id=6323181871148566277>🇮🇳</emoji> India ➪ {hrs[8]}\n<emoji id=6323570711717742330>🇫🇷</emoji> France ➪ {hrs[3]}\n<emoji id=6323453751168337485>🇨🇳</emoji> China ➪ {hrs[9]}\n<emoji id=6321003171678259486>🇹🇷</emoji> Turkey ➪ {hrs[0]}\n<emoji id=6323602322677040561>🇨🇱</emoji> Mongolia ➪ {hrs[10]}\n<emoji id=6323325327351219831>🇨🇦</emoji> Canada ➪ {hrs[11]}\n<emoji id=6323471399188957082>🇮🇹</emoji> Italia ➪ {hrs[2]}\n<emoji id=6323516260122363644>🇪🇬</emoji> Egypt ➪ {hrs[3]}\n<emoji id=6323236391463421376>🇦🇲</emoji> Armenia ➪ {hrs[12]}\n\n<emoji id=5188216117272780281>🍙</emoji> #Shizu"


@loader.module(name="UniversalTime", author="shizumods")
class UniversalTimeMod(loader.Module):
    """See the time of other countries"""

    @loader.command()
    async def atimecmd(self, app, message):
        """See global time"""
        kk = check_time()
        await utils.answer(message, kk)
