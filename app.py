from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/api/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
<<<<<<< HEAD
    vscode
=======
    GitHub
>>>>>>> 26427bbbee71cefe552303c365882c47f46fab19
