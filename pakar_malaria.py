gejala_pasien = []

def tanya_gejala(kode_gejala, teks_pertanyaan):
    jawaban = input(f"{teks_pertanyaan} (y/t): ").lower()

    if jawaban == 'y':
        gejala_pasien.append(kode_gejala)

def jalankan_diagnosa():
    print("\n--- Hasil Analisis Sistem ---")

    terdeteksi = False

    if "nyeri_otot" in gejala_pasien and "muntah" in gejala_pasien and "kejang" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Tertiana")
        terdeteksi = True

    if "nyeri_otot" in gejala_pasien and "menggigil" in gejala_pasien and "tidak_enak_badan" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Quartana")
        terdeteksi = True

    if "keringat_dingin" in gejala_pasien and "sakit_kepala" in gejala_pasien and "mimisan" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Tropika")
        terdeteksi = True

    if not terdeteksi:
        print(">> Tidak terdeteksi penyakit malaria berdasarkan gejala yang Anda masukkan.")

def main():
    print("=== SISTEM PAKAR DIAGNOSA MALARIA ===")
    print("Jawablah pertanyaan berikut dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

    tanya_gejala("nyeri_otot", "Apakah Anda mengalami nyeri otot?")
    tanya_gejala("muntah", "Apakah Anda mengalami muntah?")
    tanya_gejala("kejang", "Apakah Anda mengalami kejang?")
    tanya_gejala("menggigil", "Apakah Anda mengalami menggigil?")
    tanya_gejala("tidak_enak_badan", "Apakah Anda merasa tidak enak badan?")
    tanya_gejala("demam", "Apakah Anda mengalami demam?")
    
    jalankan_diagnosa()

main()