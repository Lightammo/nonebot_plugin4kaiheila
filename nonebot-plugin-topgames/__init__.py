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

from nonebot import get_driver

from .func import *


topGames = on_command("tg")


@topGames.handle()
async def topGames_escape(message: Message = CommandArg()):
    url = "https://store.steampowered.com/stats/"
    steamHTMLText = getHTMLText(url)
    gameList = getTopGamesList(steamHTMLText)
    await topGames.send("依据当前玩家人数排列的最热门游戏")
    await topGames.send("当前玩家人数\t今日峰值\t游戏")
    for i in range(5):
        str = '\t'.join(gameList[i])
        await topGames.send(str)
