const API_URL = 'http://localhost:5000/mahasiswa';

async function ambilMahasiswa() {
    const res = await fetch(API_URL);
    const data = await res.json();
    tampilkanMahasiswa(data);
}

function tampilkanMahasiswa(mahasiswa) {
    const daftar = document.getElementById('daftar-mahasiswa');
    daftar.innerHTML = '';

    mahasiswa.forEach(mhs => {
        const card = document.createElement('div');
        card.className = 'card flex justify-between items-center animate__animated animate__fadeInUp';

        card.innerHTML = `
            <div>
                <h3 class="text-xl font-semibold">${mhs.nama}</h3>
                <p class="text-gray-600">${mhs.nim} - ${mhs.jurusan}</p>
            </div>
            <div class="space-x-2">
                <button onclick="editMahasiswa(${mhs.id}, '${mhs.nama}', '${mhs.nim}', '${mhs.jurusan}')" class="btn btn-primary">✏️ Edit</button>
                <button onclick="hapusMahasiswa(${mhs.id})" class="btn btn-danger">🗑️ Hapus</button>
            </div>
        `;

        daftar.appendChild(card);
    });
}

document.getElementById('form-mahasiswa').addEventListener('submit', async function(e) {
    e.preventDefault();

    const nama = document.getElementById('nama').value;
    const nim = document.getElementById('nim').value;
    const jurusan = document.getElementById('jurusan').value;

    await fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nama, nim, jurusan})
    });

    this.reset();
    ambilMahasiswa();
});

async function hapusMahasiswa(id) {
    if (confirm('Yakin ingin hapus data mahasiswa ini?')) {
        await fetch(`${API_URL}/${id}`, {method: 'DELETE'});
        ambilMahasiswa();
    }
}

function editMahasiswa(id, nama, nim, jurusan) {
    const namaBaru = prompt('Edit Nama:', nama);
    const nimBaru = prompt('Edit NIM:', nim);
    const jurusanBaru = prompt('Edit Jurusan:', jurusan);

    if (namaBaru && nimBaru && jurusanBaru) {
        fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                nama: namaBaru,
                nim: nimBaru,
                jurusan: jurusanBaru
            })
        }).then(() => ambilMahasiswa());
    }
}

document.addEventListener('DOMContentLoaded', ambilMahasiswa);