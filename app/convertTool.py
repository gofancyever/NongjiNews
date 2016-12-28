
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
    content_left = soup.find(class_=re.compile('content_left'))
    title = content_left.h1.string
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









