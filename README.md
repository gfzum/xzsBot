## 致诚书院学生发展中心小助手bot

### Intro

基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 和 [nonebot](https://github.com/nonebot/nonebot) 的简单机器人实现。

### Requirements.txt

```
nonebot
openpyxl
apscheduler
jinja2<3.1.0
werkzeug<2.1.0
openpyxl<2.4.9
```

### 常规功能

使用 `xzs` + 关键词 查看信息

| 功能 | 关键词 |
| ---- | ----- |
| 获取在线文档 | `doc` `文档` `答疑` `在线文档` `在线答疑`  |
| 书院公众号二维码 | `gzh` `qrcode` `ewm` `二维码` `公众号` `推送`  |
| 书院手册获取 | `man` `手册` |
| 书院导师信息 | `ds` `tea` `导师` |
| 帮助 | `help`, `帮助` |

### Boss 功能

- 自动转发小助手私信至 boss 群聊

| 功能 | 关键词 |
| ---- | ----- |
| 今日生日查看 | `today`, `brd`, `生日`  |
| 总生日表查看 | `table`, `生日表` |
| 每月生日查看 | `month`|
| boss排班查看 | `boss`, `排班` |

### Upcoming

- Auto Birthday reminder
- command words blacklist
- Relpy to new messages in QQ group
- ddl reminder
- Fun games
- NLP
- Dockerfile and CI

If you have more interesting ideas, please feel free to contact me.
