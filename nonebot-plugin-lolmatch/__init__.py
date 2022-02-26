# 事件响应器函数
import os
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot import on_command, on_startswith
# rule事件响应规则（需要@bot才能响应事件）
from nonebot.rule import to_me
# bot使用的对象和字典
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

# 使用无头浏览器访问api地址
import urllib3
# 处理api返回的json数据
import json

from .func import *


LPLLIVE = on_command("lpllive")


@LPLLIVE.handle()
async def topGames_escape(message: Message = CommandArg()):
    url = "https://www.wanplus.com/lol/schedule"
    lplHTMLText = getHTMLText(url)
    matchData = getMatchList(lplHTMLText)
    msg = strLiveList(matchData)
    await LPLLIVE.send("尝试查找ing...\n")
    if(msg == ""):
        await LPLLIVE.send("未查询到比赛信息")
    else:
        await LPLLIVE.send(msg)
