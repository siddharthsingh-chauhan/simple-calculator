"""Flask web server for the calculator application."""

from flask import Flask, render_template, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route('/')
def index():
    """Serve the calculator UI."""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """Perform a calculation and return the result.

    Expects JSON with: num1, num2, operation
    Returns JSON with: result or error
    """
    data = request.get_json()

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        # Return integer if result is whole number
        if result == int(result):
            result = int(result)

        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid request data'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
