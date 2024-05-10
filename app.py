from flask import Flask, jsonify

app = Flask(__name__)

def factorial(numero):
    if numero == 0:
        return 1
    elif numero < 0:
        return "Error: El numero debe ser positivo"
    else:
        factorial = 1
        while numero > 0:
            factorial = factorial * numero
            numero -= 1
        return factorial

@app.route('/<id>')
def calculate(id):
    factorial_value = factorial(int(id))
    if isinstance(factorial_value, int):
        return jsonify({'factorial': factorial_value})
    else:
        return jsonify({'error': factorial_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
