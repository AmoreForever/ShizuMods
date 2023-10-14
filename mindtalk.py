# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# module made by https://t.me/AstroModules
# special thanks to @toxicuse

# banner: https://github.com/AmoreForever/shizuassets/blob/master/mindtalk.jpg?raw=true


from .. import loader, utils
import requests


@loader.module("MindTalk", "hikamoru")
class MindTalkMod(loader.Module):
    """Your little psychologist Based on MindTalk by Hikamoru"""

    strings = {
        "args_error": "<emoji id=5273793379300289907>❗️</emoji> <b>Missing or invalid arguments!</b>",
        "successful_login": "<emoji id=5206607081334906820>✔️</emoji> <b>Login completed successfully. Token saved in config</b>",
        "not_token": "<emoji id=5210952531676504517>❌</emoji>  <b>Missing access token. Please login using the <code>{}login</code> command</b>",
        "wait": "<emoji id=5310192647313301616>☕️</emoji> <b>Waiting answer from a psychologist...</b>",
        "login_error": (
            "<emoji id=5210952531676504517>❌</emoji> "
            "<b>Login failed. You may have entered the wrong password or you are not registered. "
            'Try again, or go through the authorization again using <a href="https://t.me/hikpsybot?start=register">this link.</a></b>'
        ),
        "answer": (
            "<emoji id=5818995853544656277>👩‍💻</emoji> "
            "<b>Your question:</b> {}\n\n"
            "<emoji id=5431602426354344379>👩‍⚕️</emoji> "
            "<b>Answer from psychologist:</b> {}"
        ),
        "history_cleared": "<emoji id=5818967120213445821>🛡</emoji> <b>Your history has been successfully cleared</b>",
    }

    strings_ru = {
        "args_error": "<emoji id=5273793379300289907>❗️</emoji> <b>Отсутствуют или неверные аргументы!</b>",
        "successful_login": "<emoji id=5206607081334906820>✔️</emoji> <b>Вход успешно выполнен. Токен сохранен в конфиге</b>",
        "not_token": "<emoji id=5210952531676504517>❌</emoji>  <b>Отсутствует токен доступа. Пожалуйста, выполните вход с помощью команды <code>{}login</code></b>",
        "wait": "<emoji id=5310192647313301616>☕️</emoji> <b>Ожидание ответа от психолога...</b>",
        "login_error": (
            "<emoji id=5210952531676504517>❌</emoji> "
            "<b>Ошибка входа. Возможно вы ввели неверный пароль или вы не зарегистрированы. "
            'Попробуйте еще раз, либо пройдите авторизацию заново, используя <a href="https://t.me/hikpsybot?start=register">эту ссылку.</a></b>'
        ),
        "answer": (
            "<emoji id=5818995853544656277>👩‍💻</emoji> "
            "<b>Ваш вопрос:</b> {}\n\n"
            "<emoji id=5431602426354344379>👩‍⚕️</emoji> "
            "<b>Ответ от психолога:</b> {}"
        ),
        "history_cleared": "<emoji id=5818967120213445821>🛡</emoji> <b>Ваша история успешно очищена</b>",
    }

    strings_uz = {
        "args_error": "<emoji id=5273793379300289907>❗️</emoji> <b>Argumentlar yo'q yoki noto'g'ri!</b>",
        "successful_login": "<emoji id=5206607081334906820>✔️</emoji> <b>Kirish muvaffaqiyatli yakunlandi. Token saqlandi</b>",
        "not_token": "<emoji id=5210952531676504517>❌</emoji>  <b>Token yo'q. Iltimos, <code>{}login</code> buyrug'ini ishlatib kirishni amalga oshiring</b>",
        "wait": "<emoji id=5310192647313301616>☕️</emoji> <b>Psixologdan javobni kutish...</b>",
        "login_error": (
            "<emoji id=5210952531676504517>❌</emoji> "
            "<b>Kirishda xatolik. Ehtimol, siz noto'g'ri parol kiritdingiz yoki ro'yxatdan o'tmagansiz. "
            "Qayta urinib ko'ring yoki <a href=\"https://t.me/hikpsybot?start=register\">bu havoladan</a> ro'yxatdan o'ting.</b>"
        ),
        "answer": (
            "<emoji id=5818995853544656277>👩‍💻</emoji> "
            "<b>Sizning savolingiz:</b> {}\n\n"
            "<emoji id=5431602426354344379>👩‍⚕️</emoji> "
            "<b>Psixolog javobi:</b> {}"
        ),
        "history_cleared": "<emoji id=5818967120213445821>🛡</emoji> <b>Sizning tarixingiz muvaffaqiyatli tozalandi</b>",
    }

    strings_jp = {
        "args_error": "<emoji id=5273793379300289907>❗️</emoji> <b>引数がありませんまたは無効です！</b>",
        "successful_login": "<emoji id=5206607081334906820>✔️</emoji> <b>ログインに成功しました。トークンが構成に保存されました</b>",
        "not_token": "<emoji id=5210952531676504517>❌</emoji>  <b>アクセストークンがありません。 <code>{}login</code>コマンドを使用してログインしてください</b>",
        "wait": "<emoji id=5310192647313301616>☕️</emoji> <b>心理学者からの回答を待っています...</b>",
        "login_error": (
            "<emoji id=5210952531676504517>❌</emoji> "
            "<b>ログインに失敗しました。パスワードを間違えた可能性があります。または登録されていません。 "
            '<a href="https://t.me/hikpsybot?start=register">このリンクを使用して、再度認証を行います。</a></b>'
        ),
        "answer": (
            "<emoji id=5818995853544656277>👩‍💻</emoji> "
            "<b>あなたの質問：</b> {}\n\n"
            "<emoji id=5431602426354344379>👩‍⚕️</emoji> "
            "<b>心理学者からの回答：</b> {}"
        ),
        "history_cleared": "<emoji id=5818967120213445821>🛡</emoji> <b>あなたの履歴が正常にクリアされました</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "token",
            None,
            lambda m: "Here you can set your token for MindTalk. "
        )
        self.url = "https://ps.hikamoru.uz"

    async def get_token(self, login, password):
        params = {"username": login, "password": password}
        if (requests.post(self.url + "/api/authenticate", params=params)).json()[
            "result"
        ] == True:
            token = (
                requests.post(self.url + "/api/createUserToken", params=params)
            ).json()["result"]
            self.config["token"] = token
            return True
        else:
            return False

    @loader.command()
    async def login(self, app, message):
        """(login) (password) - log in and save token"""

        args = utils.get_args_raw(message)
        if not args or not args.split()[1]:
            return await utils.answer(message, self.strings("args_error"))

        login, password = args.split()
        gen = await self.get_token(login, password)
        if gen == True:
            return await utils.answer(message, self.strings("successful_login"))
        else:
            return await utils.answer(message, self.strings("login_error"))

    @loader.command()
    async def ask(self, app, message):
        """(message) - ask a psychologist a question"""

        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, self.strings("args_error"))

        if not self.config["token"]:
            return await utils.answer(
                message, self.strings("not_token").format(", ".join(self.prefix))
            )

        params = {"userMessage": args, "TOKEN": self.config["token"]}
        msg = await utils.answer(message, self.strings("wait"))
        response = (requests.post(self.url + "/api/chat", params=params)).json()
        text = response["result"]

        await utils.answer(message, self.strings("answer").format(args, text))

    @loader.command()
    async def mtclear(self, app, message):
        """clear MindTalk history"""

        if not self.config["token"]:
            return await utils.answer(
                message, self.strings("not_token").format(", ".join(self.prefix))
            )

        params = {"TOKEN": self.config["token"]}
        response = (
            requests.post(self.url + "/api/clear_chat_history", params=params)
        ).json()
        await utils.answer(message, self.strings("history_cleared"))
