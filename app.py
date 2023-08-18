from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():
    return '<h1>Hello, World Ronaldo uwu!</h1>'

@app.route('/sumita')
def suma(term1=10,term2=20):
    result=term1+term2
    return f'<h1>El resultado (por defecto) de la funcion suma es: {result}</h1>'

@app.route('/multiplicar')
def multiplicar(term1=10,term2=20):
    result=term1*term2
    return f'<h1>El resultado (por defecto) de la funcion multiplicar es: {result}</h1>'

if __name__ == '__main__':
    app.run()