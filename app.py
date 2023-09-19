from flask import Flask,render_template, redirect, url_for, request, session, flash, make_response, Response
import psycopg2  # pip install psycopg2
import psycopg2.extras
from functools import wraps
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = "calibracao"

DB_HOST = "database-1.cdcogkfzajf0.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "15512332"

def login_required(func): # Lógica do parâmetro de login_required, onde escolhe quais páginas onde apenas o usuário logado pode acessar
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'loggedin' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute(
            "SELECT * FROM calibracao.tb_usuario WHERE email = %s AND senha = %s", (username, password))
        user = cur.fetchone()
   
        if user is not None:
            session['loggedin'] = True
            session['username'] = user['email']
            return redirect(url_for('inicio'))
        else:
            pass
    return render_template("login.html")

@app.route('/logout')
def logout(): # Botão de logout
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/')
@login_required
def inicio(): 
    
    return render_template("home_calibracao.html")

@app.route('/cadastro', methods=['GET','POST'])
@login_required
def cadastro(): 

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':

        equip = request.form['tag_equipamento']
        # fabric = request.form['fabricante']
        # grandeza = request.form['grandeza']
        # unidade = request.form['unidade']
        # faixa_nominal = request.form['nominal']
        # faixa_calibracao = request.form['faixa_calibracao']
        # preco = request.form['preco']

        query = (f"""   SELECT DISTINCT (unidade,faixa_nominal)
                        FROM calibracao.tb_get_equipamentos
                        WHERE equipamento = '{equip}';""")

        cur.execute(query)
        data = cur.fetchall()
        df_data = pd.DataFrame(data)
        unidades_no_equipamento = df_data[0].values.tolist()
        print(unidades_no_equipamento)

        return render_template("cadastro.html",unidades_no_equipamento=unidades_no_equipamento)

    s = ("""SELECT DISTINCT(equipamento) 
            FROM calibracao.tb_get_equipamentos
            ORDER BY equipamento;""")

    cur.execute(s)
    data = cur.fetchall()
    df_data = pd.DataFrame(data)
    equipamentos = df_data[0].values.tolist()
    
    return render_template("cadastro.html",equipamentos=equipamentos)

@app.route('/cadastro_tag', methods=['GET','POST'])
@login_required
def cadastro_tag(): 

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':

        tag = request.form['tag']
        tag_equipamento = request.form['tag_equipamento']
        tag_nominal = request.form['tag_nominal']
        tag_unidade = request.form['tag_unidade']
        tag_localizacao = request.form['tag_localizacao']
        tag_responsavel = request.form['tag_responsavel']
        tag_controle = request.form['tag_controle']
        tag_data = request.form['tag_data']
        tag_periodicidade = request.form['tag_periodicidade']
        tag_metodo = request.form['tag_metodo']

    return render_template("cadastro.html")

@app.route('/relacao')
@login_required
def relacao(): 
    
    return render_template("relacao.html")

@app.route('/sigla', methods=['GET','POST'])
@login_required
def sigla():

    return render_template("sigla.html")

def tabela_inicial():

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    df = pd.read_excel(r'C:\Users\TI\teste\Calibração\Controle Plano Mestre de Calibração.xlsx')

    df.columns.values[4] = 'Faixa de calibração'

    df = df.iloc[:, :-1]

    df = df.fillna('')

    for i in range(len(df)):

        sql = """ INSERT INTO calibracao.tb_get_equipamentos (equipamento, faixa_nominal, unidade, grandeza, faixa_calibracao, fabricante) VALUES (%s,%s,%s,%s,%s,%s) """
        
        values = (df['Equipamento'][i], df['Faixa nominal'][i], df['Un'][i], df['Grandeza'][i], df['Faixa de calibração'][i], df['Fabricante'][i])
        
        cur.execute(sql, values)   

    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
