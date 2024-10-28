from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def mi_endpoint():
    abc = request.args.get('ABC')
    if abc == '123':
        return jsonify(result='XYZ'), 200
    else:
        return jsonify(result='Invalid input'), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

