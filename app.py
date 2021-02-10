from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


def CountingItems(items):
    countThis = 0
    countThe = 0
    countThere = 0
    for item in items:
        print(item)
        if 'this' in item.lower():
            countThis += 1
        elif 'there' in item.lower():
            countThere += 1
        elif 'the' in item.lower():
            countThe += 1
    result = {
        'countThis': countThis,
        'countThe' : countThe,
        'countThere' : countThere
        }
    print(result)
    return result


@app.route('/', methods = ['POST', 'GET'])
def HomePage():
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        f = request.files['text-file']
        file = f.read().decode('utf-8')
        items = json.dumps(file)
        items = items.replace('[','')
        items = items.replace(']','')
        items = items.replace('\\n','')
        items = items.replace('"','')
        items = items.split(',')
        print(type(items))
        result = CountingItems(items)
        return jsonify(result = result)

        
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
