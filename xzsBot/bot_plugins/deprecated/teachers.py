from nonebot.command import CommandSession
from nonebot.plugin import on_command

__plugin_name__ = '导师/ds/tea'
__plugin_usage__ = (
    '获取致诚书院2022导师信息'
)

@on_command('ds', aliases=('tea', '导师'))
async def _(session: CommandSession):
    await session.send("有关导师双选流程、小tips等事项，可以查看致诚书院公众号推送：https://mp.weixin.qq.com/s/KQGet69TEJLPuACEKeAPGA\n" + 
    "有关导师的具体介绍，可以查看”致诚书院2022宣传手册“中导师介绍部分，手册在线观看地址：https://maiimg.com/dec/a54672441378@pdf（推荐电脑下载群文件后观看，配合书签食用更佳！）\n"
    +"一些小提醒：\n" +
    "想要进一步了解书院的各个导师，可以私戳群里的大学长们单独了解喔～\n社会导师是会参与书院活动的导师，不在可以选择的生活导师范畴之内")
    