from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


def CountingItems(items):
    result=  {
        'countThis': items.count('this'),
        'countThe': items.count('the'),
        'countThose': items.count('those')
    }
    return result

@app.route('/', methods = ['POST', 'GET'])
def HomePage():
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        f = request.files['text-file']
        file = f.read().decode('utf-8')
        items = json.dumps(file)
        result = CountingItems(items.lower())
        print(result)
        return jsonify(result = result)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
