from flask import Flask
from controllers.user import blue_user
from controllers.note import blue_note
app = Flask(__name__, template_folder='views')

if __name__ == "__main__":
    app.register_blueprint(blue_user)
    app.register_blueprint(blue_note)
    app.run(debug=True)