
from app import app
from app import convertTool
@app.route('/')
def hello_world():
    url = 'http://news.nongji360.com/html/2016/12/213970.shtml'
    return convertTool.readNews(url)

