from flask import Flask, render_template, url_for, request, redirect
import mysql.connector

app = Flask(__name__)


database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'aula_13_10'
}


connection = mysql.connector.connect(**database_config)
db_cursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/novo_setor', methods=['POST'])
def novo_setor():
    if request.method == 'POST':
        setor_nome = request.form['nome']
        query = 'INSERT INTO setores (nome) VALUES (%s)'
        db_cursor.execute(query, (setor_nome,))
        connection.commit()
    return redirect(url_for('home'))

@app.route('/novo_cargo', methods=['POST'])
def novo_cargo():
    if request.method == 'POST':
        nome_cargo = request.form['cargo']
        insert_query = 'INSERT INTO cargos (nome) VALUES (%s)'
        db_cursor.execute(insert_query, (nome_cargo,))
        connection.commit()
    return redirect(url_for('home'))


@app.route('/novo_funcionario', methods=['POST'])
def novo_funcionario():
    if request.method == 'POST':
        nome = request.form['primeiro_nome']
        ultimo_nome = request.form['sobrenome']
        admissao = request.form['data_admissao']
        status = request.form['status_funcionario']
        setor_id = request.form['id_setor']
        cargo_id = request.form['id_cargo']
        funcionario_dados = (nome, ultimo_nome, admissao, status, setor_id, cargo_id)
        insert_query = (
            'INSERT INTO funcionarios '
            '(primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo) '
            'VALUES (%s, %s, %s, %s, %s, %s)'
        )
        db_cursor.execute(insert_query, funcionario_dados)
        connection.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

