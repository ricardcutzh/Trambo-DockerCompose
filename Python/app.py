#docker run --network ejercicio5 --rm -it -p 8000:8000 -v $PWD:/home trambopython:1.0 /bin/bash
#docker run --network ejercicio5 --name redis-server --rm -d redis
from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)

r = redis.Redis(
    host='redis-server',# nombre del contenedor
    port=6379
)

@app.route('/')
def home():
    data = getData()
    return render_template('home.html', data = data)

@app.route('/Note', methods=['POST'])
def save_note():
    title = request.form.get('NTitle')
    text = request.form.get('NText')
    r.set(title, text)
    return redirect('/')

def getData():
    lista = {}
    for key in r.scan_iter():
       lista[key] = r.get(key)
    return lista

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')