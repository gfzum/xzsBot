from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '中心/zx/center'
__plugin_usage__ = (
    '获取在线文档链接'
)

@on_command('doc', aliases=('中心', 'zx', 'center'))
async def _(session: CommandSession):
    await session.send("欢迎加入致诚书院学生发展中心！\n" + 
    "公众号推送介绍请看：https://mp.weixin.qq.com/s/rHiAFJFACPdJjvy6mbuv3g\n" +
    "感兴趣的话可以进入招新群和我们唠嗑噢~\n" + 
    "[CQ:image,file=https://p.sda1.dev/6/2a20b8b8d92df8a0fc84f03295c872c9/0.jpeg]" + 
    "\n原我们的爱 正中你的心！")
    
    