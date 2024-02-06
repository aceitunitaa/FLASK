from flask import Flask, render_template, request
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

datos = {
    'Emma': 'pacosanz@gmail.com',
    'Adrian': 'pedrosanchez@gmail.com',
    'David': 'argentino@gmail.com',
    'Joel': 'joelcobre@gmail.com'
}

def mail(user):
    if user in datos:
        email = datos[user]
        return email
    return 'No encontrado.'

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      user = request.form['name']
      email = request.form['correo']
      datos[user] = email
      return render_template('formulario.html',name = user, resultado = email)
   else:
      return render_template('addmail.html')

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['name']
      email = mail(user)
      return render_template('resultado.html', resultado = email)
   else:
      return render_template('formulario.html')

if __name__ == '__main__':
   app.run(debug = True)