from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    # Identificando o método da requisição
    method = request.method
    
    # Captura os parâmetros dependendo do método
    if method == 'GET':
        params = request.args
    elif method == 'POST':
        params = request.form
    elif method == 'PUT':
        params = request.form  # PUT também envia dados no corpo
    elif method == 'DELETE':
        params = request.args  # Geralmente dados de DELETE estão nos parâmetros da URL
    
    # Formatando os parâmetros para exibição
    formatted_params = "\n".join([f"{key}: {value}" for key, value in params.items()])
    
    # Retorna o método da requisição e os parâmetros
    return f"Método: {method}\nRequisição recebida com os seguintes parâmetros:\n{formatted_params}"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)
