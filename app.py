from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression', '')
    
    try:
        result = eval(expression)
        return jsonify({'result': str(result), 'error': False})
    except:
        return jsonify({'result': 'Error', 'error': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
