from flask_marshmallow import Marshmallow
from models import Mahasiswa

ma = Marshmallow()

class MahasiswaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mahasiswa
        load_instance = True