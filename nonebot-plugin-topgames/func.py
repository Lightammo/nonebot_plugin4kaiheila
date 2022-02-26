import requests
from bs4 import BeautifulSoup
gameList = []


def getHTMLText(url):  # 常用的HTML文本获取
    try:
        r = requests.get(url)
        r.raise_for_status()    # 检查获取 url 的情况
        r.encoding              # encoding会自动识别编码方式
        return r.text
    except:
        return ""


def getTopGamesList(steamHTMLText):
    soup = BeautifulSoup(steamHTMLText)
    gameTr = soup.find_all("tr", {"class": "player_count_row"})
    for tr in gameTr:
        singleGameData = []
        for span in tr.find_all("span", {"class": "currentServers"}):
            singleGameData.append(span.string)
        for a in tr.find_all("a", {"class": "gameLink"}):
            singleGameData.append(a.string)
        gameList.append(singleGameData)
    return gameList


def strList(gameList):
    str = "{1:{0}<4}{2:{0}<8}{3:{0}<10}{4:{0}<10}\n".format(
        (chr(12288)), "排名", "当前玩家人数", "今日峰值", "游戏")
    for i in range(10):
        g = gameList[i]  # 获取每个游戏的数据列表
        str += "{1:{0}<4}{2:{0}<8}{3:{0}<10}{4:{0}^10}\n".format(
            (chr(12288)), i+1, g[0], g[1], g[2])
    return str
