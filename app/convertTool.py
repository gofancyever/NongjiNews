
import urllib.request
import re
from bs4 import BeautifulSoup
import json
def readNews(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'lxml')
    result = {
        'title':getTitle(soup),
        'content':getContentTxt(soup),
        'image':getImg(soup)
    }
    return json.dumps(result)

def getTitle(soup):
    content = soup.find(class_=re.compile('basic'))
    title = content.h1.string
    return title

def getContentTxt(soup):
    content_txt = soup.find(id = 'article_content')
    array = []
    for p in content_txt.strings:
        array.append(p)
    return array

def getImg(soup):
    content_txt = soup.find(id = 'article_content')
    array = []
    for img in content_txt.find_all('img'):
        array.append(img.get('src'))
    return array

def getPushTime(soup):
    content = soup.find(class_=re.compile('basic'))
    time = content.p
    return time.string


def getTable(soup):
    table = soup.tbody
    trs = table.find_all('tr')
    for tr in trs:
        for tb in tr.find_all('td'):
            print(tb.string)


    # for tb in tr:
        # print(tb)

url = "http://weixin.nongji360.com/news/view.php?id=213922"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,'lxml')
# print(getTitle(soup))
# print(getPushTime(soup))
getTable(soup)



