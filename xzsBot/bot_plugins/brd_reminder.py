from nonebot.command import CommandSession
from nonebot.plugin import on_command
import pytz
from datetime import datetime
from openpyxl import load_workbook
from aiocqhttp.exceptions import Error as CQHttpError

# get sheet1
bd_sheet = load_workbook('/home/gfzum/Scripts/xzs/xzsBot/data/birthday.xlsx').active

birthday_map = {}
show_birthday = "生日表\n"

for row in bd_sheet:
    if row[0].value != 'date':
        date = str(row[0].value).replace('.', '-')
        name = row[1].value.replace('\n',' 和 ')
        birthday_map[date] = name
        show_birthday += date + " " + name + "\n"

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


@on_command('today', aliases=('生日','brd'))
async def _(session: CommandSession):
    
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    today = f"{now.year}年{now.month}月{now.day}日"
    str_today = str(now.month) + "-" + str(now.day)

    celebrate = ""
    if(str_today not in birthday_map):
        celebrate = '无人贺生～'
    else:
        celebrate = f'{birthday_map[str_today]}过生日哦～'

    msg = f'今天是{today}，{celebrate}'
    await session.send(msg)


@on_command('生日表', aliases=('brdtable','table'))
async def _(session: CommandSession):
    await session.send(show_birthday)