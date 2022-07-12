from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '公众号 / gzh / 二维码'
__plugin_usage__ = (
    '获取致诚书院公众号二维码'
)

@on_command('gzh', aliases=('二维码', '公众号', 'qrcode', 'ewm', '推送'))
async def _(session: CommandSession):
    await session.send("欢迎关注致诚书院公众号，查看迎新推送！\n" + 
    "[CQ:image,file=https://p.sda1.dev/6/c9480923301059ea84cd9c63b1a48bde/致诚公众号二维码.jpg]")
    