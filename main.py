from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def main_get():
    return render_template('index.html')

@app.route('/text_trans', methods=['POST', 'GET'])
def text_trans():
    if request.method == 'POST':
        temp = request.form['local']
    elif request.method == 'GET':
        temp = request.args.get('local')
        temp = temp + '지역 데이터 보여주기'
    
    return render_template('index.html', local=temp)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


