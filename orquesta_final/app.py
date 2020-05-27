from flask import Flask, render_template
from logica.grupoOrquesta import grupoOrquesta

app = Flask(__name__)


@app.route('/Orquesta')
def index():
    b = grupoOrquesta()
    return render_template('Orquesta.html', assignedgrupoOrquesta=b.asignargrupoOrquesta(), afinargrupoOrquesta=b.afinargrupoOrquesta(), tocargrupoOrquesta=b.tocargrupoOrquesta())

@app.route('/')
def inicio():
    return render_template('Index.html')

if __name__ == "__main__":
    app.run(debug=True)
