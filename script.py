from flask import Flask, request, render_template
import nexmo

app = Flask(__name__)
client = nexmo.Client(key='ce9f1f15', secret='sRSeARGzTNaA3iXM')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
	numero = request.form['numero']
	mensagem = request.form['mensagem']

	response = client.send_message({
		'from': 'SEU_NUMERO_NEXMO',
		'to': numero,
		'text': mensagem
	})

	if response['messages'][0]['status'] == '0':
		return 'Mensagem enviada com sucesso!'
	else:
		return 'Houve um erro ao enviar a mensagem.'

if __name__ == '__main__':
	app.run(debug=True)
