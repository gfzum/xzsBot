from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '文档/doc'
__plugin_usage__ = (
    '获取在线文档链接'
)

@on_command('doc', aliases=('文档', 'document', '答疑', '在线文档', '在线答疑'))
async def _(session: CommandSession):
    await session.send("欢迎查看过往答疑，写下你的问题！\n" + 
    "https://docs.qq.com/sheet/DZUNXbHRpZEdqSWZH?u=5ee2f3bfee05418ca91d9059048040b0")