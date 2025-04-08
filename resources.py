from flask_restful import Resource, reqparse
from models import db, Mahasiswa
from schemas import MahasiswaSchema

mahasiswa_schema = MahasiswaSchema()
mahasiswas_schema = MahasiswaSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('nama', type=str, required=True, help='Nama harus diisi')
parser.add_argument('nim', type=str, required=True, help='NIM harus diisi')
parser.add_argument('jurusan', type=str, required=True, help='Jurusan harus diisi')

class MahasiswaListResource(Resource):
    def get(self):
        mhs = Mahasiswa.query.all()
        return mahasiswas_schema.dump(mhs), 200

    def post(self):
        args = parser.parse_args()
        new_mhs = Mahasiswa(
            nama=args['nama'],
            nim=args['nim'],
            jurusan=args['jurusan']
        )
        db.session.add(new_mhs)
        db.session.commit()
        return mahasiswa_schema.dump(new_mhs), 201

class MahasiswaResource(Resource):
    def get(self, mhs_id):
        mhs = Mahasiswa.query.get_or_404(mhs_id)
        return mahasiswa_schema.dump(mhs), 200

    def put(self, mhs_id):
        mhs = Mahasiswa.query.get_or_404(mhs_id)
        args = parser.parse_args()
        mhs.nama = args['nama']
        mhs.nim = args['nim']
        mhs.jurusan = args['jurusan']
        db.session.commit()
        return mahasiswa_schema.dump(mhs), 200

    def delete(self, mhs_id):
        mhs = Mahasiswa.query.get_or_404(mhs_id)
        db.session.delete(mhs)
        db.session.commit()
        return '', 204