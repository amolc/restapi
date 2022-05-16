from flask import Flask, send_from_directory
import path

app = Flask(__name__)


@app.route('/admin/<path:filename>')
def admin(filename):
    print(filename)
    if(filename==""):
        print("no filename")
    return send_from_directory(app.root_path + '/admin/', filename)

@app.route('/angular/<path:filename>')
def angular(filename):
    print(filename)
    if(filename==""):
        print("no filename")
    return send_from_directory(app.root_path + '/angular/', filename)

@app.route('/<path:filename>')
def second_income(filename):
    print(filename)
    if(filename==""):
        print("no filename")
    return send_from_directory(app.root_path + '/second_income/', filename)

@app.route('/superadmin/<path:filename>')
def superadmin(filename):
    print(filename)
    if(filename==""):
        print("no filename")
    return send_from_directory(app.root_path + '/superadmin/', filename)


@app.route('/<path:filename>')
def jwt(filename):
    print(filename)
    if(filename==""):
        print("no filename")
    return send_from_directory(app.root_path + '/jwt/public', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001,debug=True)
    