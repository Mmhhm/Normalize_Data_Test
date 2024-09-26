from flask import Flask
import psycopg2
from blueprints.missions import missions_bp
from db import db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:LightAndMic!@localhost:5432/wwii_missions"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.register_blueprint(missions_bp)


if __name__ == '__main__':
    app.run()