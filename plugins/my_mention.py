from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@respond_to('夢占い')
def mention_func(message):
    message.reply(‘hi how are u’) # メンション
    import scraping.py
