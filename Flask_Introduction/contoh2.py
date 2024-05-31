from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/operasi', methods=['POST'])
def operasi():
    data = request.get_json()

    if 'angka1' not in data or 'angka2' not in data:
        return jsonify({'error': 'Mohon berikan dua angka'}), 400

    angka1 = data['angka1']
    angka2 = data['angka2']

    hasil = {
        'penjumlahan': angka1 + angka2,
        'pengurangan': angka1 - angka2,
        'perkalian': angka1 * angka2
    }

    # Menghindari pembagian dengan nol
    if angka2 != 0:
        hasil['pembagian'] = angka1 / angka2

    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True)
