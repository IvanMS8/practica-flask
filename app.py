from flask import Flask, render_template, request

app = Flask(__name__)

# Página de Inicio
@app.route('/')
def home():
    return render_template('home.html')

# Página Quiénes Somos
@app.route('/quienes-somos')
def about():
    return render_template('about.html')

# Página de Servicios
@app.route('/servicios')
def services():
    return render_template('services.html')

# Página de Noticias
@app.route('/noticias')
def news():
    return render_template('news.html')

# Página de Contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        # Aquí puedes manejar el formulario (guardar datos, enviar correo, etc.)
        return f"Gracias {nombre}, tu mensaje ha sido recibido."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
