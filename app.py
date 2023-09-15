from flask import Flask,render_template, redirect, url_for, request, session, flash, make_response, Response

app = Flask(__name__)
app.secret_key = "calibracao"


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
            return redirect(url_for('inicio'))

    return render_template('login.html')

@app.route('/')
def inicio(): 
    
    return render_template("home_calibracao.html")

@app.route('/cadastro')
def cadastro(): 
    
    return render_template("cadastro.html")

@app.route('/relacao')
def relacao(): 
    
    return render_template("relacao.html")


if __name__ == '__main__':
    app.run(debug=True)
