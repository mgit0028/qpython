from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    num = [10, 20, 30, 50, 15, 25]
    return json.dumps({"num": num}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=1)
