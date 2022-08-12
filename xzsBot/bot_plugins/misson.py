from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '报到/bd'
__plugin_usage__ = (
    '获取报到任务在线文档链接'
)

@on_command('doc', aliases=('bd', '报到'))
async def _(session: CommandSession):
    await session.send("请各位新生在报到前务必填写该报到信息表，在中高风险地区的同学尽快与本班大学长联系。"+
    "https://docs.qq.com/sheet/DZXR3aVhtcGplVlBz\n\n" +
    "报到前，除防疫相关要求外，还需要完成12项报到任务，请在完成后填写如下表格：" + 
    "https://docs.qq.com/sheet/DZWF0eGNwTG9uY2xr\n\n"+
    "更多问题和信息，请补充或查看在线答疑文档：" + 
    "https://docs.qq.com/sheet/DZUNXbHRpZEdqSWZH\n\n")