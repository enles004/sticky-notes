from flask import Flask
from flask_cors import CORS

from controllers.note import blue_note
from controllers.user import blue_user

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


app.register_blueprint(blue_user)
app.register_blueprint(blue_note)

if __name__ == "__main__":
    app.run(debug=True)