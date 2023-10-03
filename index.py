import hashlib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Cifrar la contraseña
    h = hashlib.sha256()
    hashed_string = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(hashed_string)
    
    response = {
        'message': 'La contraseña ha sido encriptada',
        'hashed_password': hashed_string
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()