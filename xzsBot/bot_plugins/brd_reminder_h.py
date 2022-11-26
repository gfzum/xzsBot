from nonebot import on_command, CommandSession, SenderRoles
from nonebot.plugin import on_command
import pytz
from datetime import datetime
from openpyxl import load_workbook
from aiocqhttp.exceptions import Error as CQHttpError
import nonebot
import os

print(os.getcwd())
print(os.listdir())

# get sheet1
bd_sheet = load_workbook('data/birthday_2022.xlsx').active

birthday_map = {}
show_birthday = "生日表\n"

for row in bd_sheet:
    if row[0].value != 'date' and row[0].value != None:
        date = str(row[0].value).replace('.', '-')
        name = row[1].value.replace('\n',' 和 ')
        birthday_map[date] = name
        show_birthday += date + " " + name + "\n"
    
        # add timer
        mad = date.split('-')
        @nonebot.scheduler.scheduled_job('cron', month=f'{mad[0]}', day=f'{mad[1]}', hour = 0)
        async def _():
            try:
                msg = today()
                await nonebot.get_bot.send_group_msg(group_id=912811025, message=msg)
            except CQHttpError:
                pass
show_birthday = show_birthday[:-1]

# now = datetime.now(pytz.timezone('Asia/Shanghai'))#.strftime('%Y-%m-%d %H:%M:%S')


# @nonebot.scheduler.scheduled_job('cron', hour='*')
# async def birthday_reminder():
#     bot = nonebot.get_bot()
#     now = datetime.now(pytz.timezone('Asia/Shanghai'))
#     today = str(now.month) + "-" + str(now.day)
#     if today in bitrhday_map:
#         try:
#             await bot.send_group_msg(group_id=912811025,
#                                  message=f'现在{now.hour}点整啦！')
#         except CQHttpError:
#             pass

#group restriction
permit_group = { 912811025 }
banned_people = { 10000, 10001 }
def foo(sender: SenderRoles):
    return (sender.is_groupchat and sender.from_group(permit_group) and not sender.sent_by(banned_people))\
    or sender.is_superuser

@on_command('today', aliases=('生日','brd'), permission=foo)
async def _(session: CommandSession):
    msg = today()
    await session.send(msg)

@on_command('生日表', aliases=('brdtable','table'), permission=foo)
async def _(session: CommandSession):
    await session.send(show_birthday)

@on_command('month', permission=foo)
async def _(session: CommandSession):
    info = month()
    await session.send(info)
    
@nonebot.scheduler.scheduled_job('cron', month='*')
async def _():
    bot = nonebot.get_bot()
    info = month()
    try:
        await bot.send_group_msg(group_id=912811025,
                                 message=info)
    except CQHttpError:
        pass


def today():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    day = now.day
    if day < 10:
        day = f"0{day}"
    else:
        day = str(day)
    today = f"{now.year}年{now.month}月{day}日"
    str_today = str(now.month) + "-" + day

    celebrate = ""
    if(str_today not in birthday_map):
        celebrate = '无人贺生～'
    else:
        celebrate = f'{birthday_map[str_today]}过生日哦～'

    msg = f'今天是{today}，{celebrate}'
    return msg

def month():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    month = str(now.month)
    
    info = f"{month}月生日表\n"

    for i in range(32):
        j = i
        if j < 10:
            j = f"0{j}"
        else:
            j = str(j)
        date = month + "-" + j
        # print(date)
        if date in birthday_map:
            info += date + " " + birthday_map[date] + "\n"
        
    return info[:-1]
