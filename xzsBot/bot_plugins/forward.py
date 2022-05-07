from nonebot import message_preprocessor
from nonebot.command import CommandSession
from nonebot.plugin import on_command
from nonebot import get_bot
from datetime import datetime


__plugin_name__ = 'forward msg'

bot = get_bot()

@bot.on_message("private")
async def private_fwd(ctx):
    userid = ctx["user_id"]
    sender = ctx["sender"]["nickname"]
    time = ctx["time"]
    # text = ctx["message"][0]["data"]["text"]
    m = ctx["message"]

    msg = "收到一条消息\n QQ：{}\n 昵称：{}\n {}".format(userid, sender, m)

    await bot.send_group_msg(group_id=912811025, message=msg)
    await bot.send_group_msg(group_id=156129667, message=msg)

# @message_preprocessor
# async def _(bot, event, manager):
#     await bot.send(private_,"tt")
