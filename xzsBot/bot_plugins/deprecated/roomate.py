from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '室友/sy/frd'
__plugin_usage__ = (
    '获取室友文档链接'
)

@on_command('doc', aliases=('室友', 'sy', 'frd', 'friend', 'roomate'))
async def _(session: CommandSession):
    await session.send("宿舍室友将在军训后自行选择，男生尽量在班内组合，女生可以在年级内自由组合" +
    "\n欢迎在在线表格查看书院同学信息，填写自己的想法～\n" + 
    "https://docs.qq.com/sheet/DSXVwUkhjZFdWS0V5")