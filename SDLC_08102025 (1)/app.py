from flask import Flask
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
from flask import render_template
if __name__ == '__main__':
        app.run(debug=True)