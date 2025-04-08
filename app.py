from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from settings import Config
from models import db
from schemas import ma
from resources import MahasiswaListResource, MahasiswaResource

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})

db.init_app(app)
ma.init_app(app)
api = Api(app)

api.add_resource(MahasiswaListResource, '/mahasiswa')
api.add_resource(MahasiswaResource, '/mahasiswa/<int:mhs_id>')

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')  # <-- Menggunakan render_template

if __name__ == '__main__':
    app.run(debug=True)