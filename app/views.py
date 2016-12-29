from flask import request
from app import app
from app import convertTool
@app.route('/',methods=["GET","POST"])
def hello_world():
    URL = request.form.get("url")
    URL = "http://weixin.nongji360.com/news/view.php?id=213922"
    return convertTool.readNews(URL)

