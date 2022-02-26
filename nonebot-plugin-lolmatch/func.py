from time import time
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):  # 常用的HTML文本获取
    try:
        r = requests.get(url)
        r.raise_for_status()    # 检查获取 url 的情况
        r.encoding = 'utf-8'          # encoding会自动识别编码方式
        return r.text
    except:
        return ""


def getMatchList(lplHTMLText):
    soup = BeautifulSoup(lplHTMLText)
    matchAll = soup.find("div", {"class": "left-box match-all"})
    matchContentLive = matchAll.find_all(
        "li", {"class": "match-content match-live"})
    # matchContent = matchAll.find_all("li", {"class": "match-content"})
    matchData = []
    # list : flag | data | time | teamA | teamB | scoreA | scoreB | matchname
    matchData.append('Live')  # flag
    matchData.append('Now')  # time
    for li in matchContentLive:
        singleMatchData = []
        # date = li.find("li", {"class": "match-title"})
        # matchData.append(date.string)  # date
        # for li in ul.find_all("li", {"class": {"match-content match-live", "match-content"}}):
        # time = li.find("div", {"class": "w10"})
        # singleMatchData.append(time.string)  # time
        for timename in li.find("div", {"class": "team"}).find_all("span"):
            singleMatchData.append(timename.string)  # teamname
            # for div in li.find_all("div", {"class":"number"}):
            #    for score in div.find_all("i"):
            #        singleMatchData.append(score.string)  # score
        matchData.append(singleMatchData)
    return matchData


def strLiveList(matchData):
    str = ""
    for teamList in matchData:
        if isinstance(teamList, list):
            str += "{0}\tvs\t{1}\n".format(teamList[0], teamList[1])
    return str

    # for i in range(1):
    #    m = matchData[i]  # 获取每个游戏的数据列表
    #    print("{1:{0}<4}{2:{0}<8}{3:{0}<10}{4:{0}^10}".format(
    #         (chr(12288)), m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7]))
