from nonebot.command import CommandSession
from nonebot.plugin import on_command, get_loaded_plugins
from services.command_use_count import record_successful_invocation

__plugin_name__ = '帮助'
__plugin_usage__ = (
    '对我说 “help” 获取可以查询的功能\n'
    '“help 功能名” 获取对应详细帮助'
)

@on_command('ping')
async def _(session: CommandSession):
    await session.send("嘤嘤嘤\nhttps://github.com/gfzum/xzsBot")


help_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

@on_command('help', aliases={'帮助'})
@record_successful_invocation('help')
async def _(session: CommandSession):
    # 获取加载的插件，注意名字以 _h 结尾的不应该被展示！
    plugins = (p for p in get_loaded_plugins() if p.name and not p.name.endswith('_h'))

    arg = session.current_arg_text.strip()
    # 没有参数：展示功能列表
    if not arg:
        await session.send(
            '有疑问欢迎随时提问or查看在线文档，群文件里有宣传手册！' + 
            '\n输入xzs (关键词)进行对应查询：\n  ' + '\n  '.join(p.name for p in plugins) +
            '\n项目介绍及源码:https://github.com/gfzum/xzsBot'
        )
    # 有参数：展示对应 usage
    else:
        for p in plugins:
            if arg.lower() in p.name.lower():
                await session.send(p.usage)