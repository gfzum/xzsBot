from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession, SenderRoles
from nonebot.plugin import on_command

__plugin_name__ = 'ddl 提醒服务'
__plugin_usage__ = (
    '设置你的ddl！'
)

permit_group = { 912811025 }
banned_people = { 10000, 10001 }
def foo(sender: SenderRoles):
    return (sender.is_groupchat and sender.from_group(permit_group) and not sender.sent_by(banned_people))\
    or sender.is_superuser

@on_command('ddl', aliases=('list'), permission=foo)
async def _(session: CommandSession):

    # 取得消息的内容，并且去掉首尾的空白符
    info = session.current_arg_text.strip().split(' ')
    if not info or info[0] == '':
        nonebot.scheduler.print_jobs()
        msg = str(nonebot.scheduler.get_jobs())
        msg += '\n 使用 ddl 日期 时间 来添加ddl哦'
        await session.send(msg)
    elif len(info) == 1:
        time = (await session.aget(prompt='你想在什么时候收到提醒呢？')).strip()
        # 如果用户只发送空白符，则继续询问
        while not time:
            time = (await session.aget(prompt='时间不能为空呢，请重新输入')).strip()
        info.append(time)

    user_id = session.ctx['user_id']
    sender = session.ctx["sender"]["nickname"]
    msg = f"添加成功！f{sender} f{user_id}，你的ddl为{str(info)}"
    # 向用户发送天气预报
    await session.send(msg)