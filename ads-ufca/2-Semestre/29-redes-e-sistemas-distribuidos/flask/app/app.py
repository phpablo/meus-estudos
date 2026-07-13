from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_data():
    data = request.form['data']
    return f'Os dados recebidos foram: {data}'

@app.route('/receive', methods=['GET'])
def receive_data():
    data = request.args.get('data')
    return f'Os dados enviados via GET foram: {data}'

@app.route('/sum', methods=['GET'])
def page2():
    return render_template('page2.html')

@app.route('/get_sum/<int:n1>/<int:n2>', methods=['GET'])
def soma(n1,n2):
    return f'Soma dos numeros {n1 + n2}'

@app.route('/sum', methods=['POST'])
def post_sum_data():
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    return f'A soma dos dois valores do forms é: {n1 + n2}'

if __name__ == '__main__':
    app.run()