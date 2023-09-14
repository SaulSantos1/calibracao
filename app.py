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
def solda(): 
    
    return render_template("cadastro.html")

@app.route('/pintura')
def pintura(): 
    
    return render_template("pintura.html")


if __name__ == '__main__':
    app.run(debug=True)
