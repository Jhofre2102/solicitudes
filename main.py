from flask import Flask,request,render_template,make_response




app=Flask(__name__)

@app.route("/")
def inicio():
    return "Pagina de Inicio"

#ruta parametros Url
@app.route("/consulta")
def ruta_consulta():
    producto=request.args.get("product")
    talla=request.args.get("talla")
    if producto and talla is None:
        return f"Se esta consultando solo el producto {producto}"
        
    if talla is None  and producto:
        return f" Por favor ingrese el producto a buscar {talla}"
    
    if producto is None and talla is None:
        return f"Bienvenido a la pagina de Ropa"
    return f"Se esta consultando el producto {producto} y la talla {talla}"

    
    
#ruta para capturar datos por el cuerpo de solicitud para el body

#muestra el formulario al usuario 
listado=[]
@app.route("/registro",methods={"GET"}) #se define la ruta
def ruta_registro():
    #listado=[{"nombre":"jhon","correo":"jhofre37@hotmail.com"}]
    return render_template("formulario.html",listado=listado)

@app.route("/registro",methods={"POST"}) #se define la ruta
def procesar_registro():
    nombre=request.form.get("nombre")
    correo=request.form.get("correo")
    estudiantes={"nombre":nombre,"correo":correo}
    listado.append(estudiantes)
    
    
    
    #print (nombre)
    return f"El estudiante quedo registrado como : {nombre} y su correo es {correo}"
    
    
#parametros en la ruta
@app.route("/estudiantes/<string:area>/<int:grupo>")
def mostrar_estudiantes(grupo,area):
     return f"El programa de formacion consultado es {area} y el grupo consultado es {grupo}"
     
 
#Encabezados HTTP Hypertext Transfer Protocol
 
@app.route('/ver-headers')
def ver_headers():
    agente_usuario = request.headers.get('User-Agent')
    return f"Tu navegador es: {agente_usuario}"


#gestion de las cookies

@app.route('/crear-cookie')
def crear_cookie():
 respuesta = make_response("Cookie creada!") # es un mensaje del navegador
 respuesta.set_cookie('usuario_logeado', 'true',max_age=60*60*24,httponly=True)
 return respuesta


@app.route('/leer-cookie')
def leer_cookie():
 valor = request.cookies.get('usuario_logeado')
 return f"Valor de la cookie: {valor}"




if __name__=="__main__":
    app.run(debug=True)