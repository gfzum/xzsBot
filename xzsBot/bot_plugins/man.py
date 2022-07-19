from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '手册/man/manual'
__plugin_usage__ = (
    '获取致诚书院2022迎新手册'
)

@on_command('man', aliases=('manual', '手册'))
async def _(session: CommandSession):
    await session.send("欢迎查看群文件中的\"2022致诚迎新手册.pdf\"～\n" + 
    "在线阅读链接（推荐电脑下载群文件后a观看，配合书签食用更佳！）：https://maiimg.com/dec/a54672441378@pdf")
    