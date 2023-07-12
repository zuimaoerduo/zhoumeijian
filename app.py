from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/baiduzhishu.html')
def baiduzhishu():  # put application's code here
    return render_template('baiduzhishu.html')

@app.route('/ciyunfenxi.html')
def ciyunfenxi():  # put application's code here
    return render_template('ciyunfenxi.html')

@app.route('/qingganzhishu.html')
def qingganzhishu():  # put application's code here
    return render_template('qingganzhishu.html')
if __name__ == '__main__':
    app.run()
