from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['name']
      return render_template('resultado.html')
   else:
      return render_template('formulario.html')

if __name__ == '__main__':
   app.run(debug = True)

@app.route("/")
def hola():
    return "Hello World!"

@app.route("/numero/<int:imparopar>")
def secret(imparopar):
    if imparopar %2 == 0:
        return "Es par."
    else:
        return "Es impar."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/edat100/<name>/<int:edat>')
def edat(name,edat):
    resta = 100 - edat
    años = 2024 + resta
    return render_template('edat.html', name=name, años=años)
