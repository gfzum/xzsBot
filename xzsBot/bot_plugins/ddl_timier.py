from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession, SenderRoles
from nonebot.plugin import on_command
import re

__plugin_name__ = 'ddl 提醒服务'
__plugin_usage__ = (
    '设置你的ddl！'
)

permit_group = { 912811025 }
banned_people = { 10000, 10001 }
def foo(sender: SenderRoles):
    return (sender.is_groupchat and sender.from_group(permit_group) and not sender.sent_by(banned_people))\
    or sender.is_superuser

@on_command('ddl', aliases=('list') )
async def _(session: CommandSession):

    msg = '添加ddl的格式如下：\n日期（使用.或-分隔） 时间（[0-23]:[0-59]） 事件\n示例:xzs ddl 12.20 19:00 校庆晚会'

    # 取得消息的内容，并且去掉首尾的空白符
    info = session.current_arg_text.strip().split(' ')
    if not info or info[0] == '':
        # nonebot.scheduler.print_jobs()
        # msg = str(nonebot.scheduler.get_jobs())
        # msg = '添加ddl的格式如下：日期（使用.或-分隔） 时间（[0-23]:[0-59]） 事件\n事例：xzs ddl 12.20 19:00 校庆晚会'
        await session.send(msg)
        return 
    
    elif len(info) != 3:
        msg = '输入的格式不对哦\n' + msg
        await session.send(msg)
        return

    mad = re.split('-|\.', info[0])
    if len(mad) != 2 or not mad_check(mad[0], mad[1]):
        msg = '输入的日期格式不对哦\n' + msg
        await session.send(msg)
        return

    time = re.split(":|：", info[1])
    if len(time) != 2 or not time_check(time[0], time[1]):
        msg = '输入的时间格式不对哦\n' + msg
        await session.send(msg)
        return 

    event = info[2]
    if event == '':
        msg = '输入的事件不能为空呢\n' + msg
        await session.send(msg)
        return
    
    user_id = session.ctx['user_id']
    sender = session.ctx["sender"]["nickname"]
    group_id = session.ctx['group_id']

    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    msg = f"添加成功！{sender}，你在{now.year}年{mad[0]}月{mad[1]}日 {time[0]}:{time[1]}分 添加了ddl：{event}"

    @nonebot.scheduler.scheduled_job('cron', month=mad[0], day=mad[1], hour = time[0], minute=time[1])
    async def _():
        try:
            msg = f'亲爱的{sender}，你设置的ddl提示到了：{event}'
            await nonebot.get_bot().send_group_msg(group_id=group_id, message=msg)
            await nonebot.get_bot().send_private_msg(user_id=user_id, message=msg)
        except CQHttpError:
            pass

    await session.send(msg)
    # nonebot.scheduler.print_job()


def mad_check(month, day):
    m = int(month)
    d = int(day)
    if m < 1 or m > 12:
        return False

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d > days[m - 1] or d < 1:
        return False

    return True

def time_check(hour, minute):
    h = int(hour)
    m = int(minute)
    return 0 <= h and h <= 23 and 0 <= m and m <= 59