from flask import Flask, render_template, request, url_for
from sp_connect import data_update

app = Flask(__name__)

@app.route('/')
def main_get():
    return render_template('index.html')

@app.route('/local_input', methods=['POST', 'GET'])
def local_input():
    if request.method == 'POST':
        local_name = request.form['local']
    elif request.method == 'GET':
        local_name = request.args.get('local')
        data_update(local_name)
    
    return render_template('index.html', local=local_name)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


