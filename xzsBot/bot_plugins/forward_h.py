from nonebot import message_preprocessor
from nonebot.command import CommandSession
from nonebot.plugin import on_command
from nonebot import get_bot, on_request
from datetime import datetime
from nonebot.helpers import send_to_superusers
from nonebot.notice_request import RequestSession


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

    print(m)
    print("\n")

    await bot.send_group_msg(group_id=912811025, message=msg)
    # await bot.send_group_msg(group_id=156129667, message=msg)

# @message_preprocessor
# async def _(bot, event, manager):
#     await bot.send(private_,"tt")

@on_request('friend', 'group.invite')
async def _(session: RequestSession):
    bot = session.bot
    event = session.event
    if event.detail_type == 'friend':
        msg = f'用户 {event.user_id} 请求添加好友。消息：{event.comment}'
    else:  # == 'group'
        msg = f'用户 {event.user_id} 邀请加入群 {event.group_id}。消息：{event.comment}'

    # 如果邀请者是超级用户，那么就自动同意请求
    if event.user_id in bot.config.SUPERUSERS:
        await session.approve()
        msg += '（已自动接受）'

    # 给超级用户发送这条消息
    # await send_to_superusers(bot, msg)
    
    await bot.send_group_msg(group_id=912811025, message=msg)

    # TODO: 使用 broadcast() 广播这条消息到监控面板