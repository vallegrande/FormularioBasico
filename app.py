from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a MySQL
config = {
    'host': 'localhost',
    'port': 33060,  # asegúrate de usar el puerto correcto
    'user': 'root',
    'password': 'entrecodigosycafe',  # tu contraseña si tienes
    'database': 'formulario_db'
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            nombre = request.form.get("nombre")
            apellidos = request.form.get("apellidos")
            correo = request.form.get("correo")
            telefono = request.form.get("telefono")
            sexo = request.form.get("sexo")
            ciudad = request.form.get("ciudad")
            edad = request.form.get("edad")
            ocupacion = request.form.get("ocupacion")
            fecha = request.form.get("fecha")

            query = """
                INSERT INTO datos 
                (nombre, apellidos, correo, telefono, sexo, ciudad, edad, ocupacion, fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (nombre, apellidos, correo, telefono, sexo, ciudad, edad, ocupacion, fecha)

            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()

            return redirect("/datos")
        except Exception as e:
            return f"Error al guardar en base de datos: {e}"

    return render_template("index.html")


@app.route("/datos")
def datos():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM datos ORDER BY id DESC")
        registros = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("datos.html", registros=registros)
    except Exception as e:
        return f"Error al obtener datos: {e}"


if __name__ == "__main__":
    app.run(debug=True)
