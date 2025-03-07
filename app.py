from flask import Flask, render_template
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    # Datos personales
    datos_personales = {
        'nombre': 'Xavi Castillo',
        'profesion': 'Tu Master Phyton',
        'email': 'xavcas@gmail.com',
        'telefono': '+34 620 037 437',
        'direccion': 'Can Ros, 32; 08027 Barcelona; Catalunya'
    }

    # Enlaces a programas (rutas locales o enlaces externos)
    programas = [
        {'nombre': 'Programa 1', 'ruta': 'C:/ruta/al/programa1.exe'},
        {'nombre': 'Programa 2', 'ruta': 'C:/ruta/al/programa2.exe'},
        {'nombre': 'Programa 3', 'ruta': 'C:/ruta/al/programa3.exe'}
    ]

    return render_template('index.html', datos=datos_personales, programas=programas)

if __name__ == '__main__':
    app.run(debug=True)
