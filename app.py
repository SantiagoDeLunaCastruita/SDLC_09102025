from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/animaleexoticos')
def animaleexoticos():
    return render_template("animalesexoticos.html")

@app.route('/carrosantiguos')
def carro_antiguos():
    return render_template("carros antiguos.html")

@app.route('/marabillasdelelmundo')
def marabillas_del_mundo():
    return render_template("marabillasdelmundo .html")

@app.route('/acercade')
def acercade():
    return render_template("acerca de.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['password']
        if usuario and contraseña:
            session['user'] = usuario  
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Datos incorrectos. Intenta nuevamente.', 'danger')
    return render_template("formulario.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['password']
        if usuario and contraseña:
            session['user'] = usuario  
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Datos incorrectos. Intenta nuevamente.', 'danger')

    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('user', None) 
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('index'))



from flask import render_template
if __name__ == '__main__':
        app.run(debug=True)