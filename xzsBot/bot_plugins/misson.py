from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '报到/bd'
__plugin_usage__ = (
    '获取报到任务在线文档链接'
)

@on_command('doc', aliases=('bd', '报到'))
async def _(session: CommandSession):
    await session.send("请在8.18前完成报到任务，并填写在表格中喔！\n" + 
    "https://docs.qq.com/sheet/DZWF0eGNwTG9uY2xr?tab=BB08J2&u=ee5339f8cb074f30b3b95d5c03a70a09")