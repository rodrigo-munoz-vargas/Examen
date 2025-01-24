from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_x_tarro = 9000
        total = precio_x_tarro * cantidad_tarros

        if 18 <= edad <= 30:
            descuento = total * 0.15
        elif edad > 30:
            descuento = total * 0.25
        else:
            descuento = 0

        total_con_descuento = total - descuento

        resultado = {
            'nombre': nombre,
            'total': total,
            'descuento': descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Usuarios ya registrados
        usuarios = {
            'juan': 'admin',
            'pepe': 'user'
        }

        # Validar usuario / password
        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido Administrador {usuario}"
            elif usuario == 'pepe':
                mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
