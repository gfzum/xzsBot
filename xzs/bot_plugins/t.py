from nonebot.command import CommandSession
from nonebot.plugin import on_command


__plugin_name__ = 't2'
__plugin_usage__ = '用法： 对我说 "小助手"，我会回复 "嘤嘤嘤"'


@on_command('ping')
async def _(session: CommandSession):
    selfId = session.self_id
    userId = session.ctx["user_id"]
    sendT = session.ctx["message_type"]
    msgT = session.ctx["message"][0]["type"]
    text = session.ctx["message"][0]["data"]["text"]

    final = "user:{}, sendType:{}, msgType:{}, text:{}".format(userId, sendT, msgT, text)
    await session.send(final)
    await session.send("嘤嘤嘤")

