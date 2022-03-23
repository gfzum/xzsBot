from nonebot.command import CommandSession
from nonebot.plugin import on_command


__plugin_name__ = 't2'
__plugin_usage__ = '用法： 对我说 "小助手"，我会回复 "嘤嘤嘤"'


@on_command('ping')
async def _(session: CommandSession):
    await session.send("嘤嘤嘤\nhttps://github.com/gfzum/xzsBot")

