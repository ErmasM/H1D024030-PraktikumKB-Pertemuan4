import tkinter as tk
from tkinter import messagebox

database_penyakit = {
    "Malaria Tertiana": ["nyeri_otot", "muntah", "kejang"],
    "Malaria Quartana": ["nyeri_otot", "menggigil", "tidak_enak_badan"],
    "Malaria Tropika": ["keringat_dingin", "sakit_kepala", "mimisan", "mual"], # Ditambahkan koma di sini
    "Malaria Pernisiosa": ["menggigil", "tidak_enak_badan", "demam", "mimisan", "mual"] 
}

semua_gejala = [
    ("nyeri_otot", "Apakah Anda merasa nyeri otot?"),
    ("muntah", "Apakah Anda mengalami muntah?"),
    ("kejang", "Apakah Anda mengalami kejang?"),
    ("menggigil", "Apakah Anda mengalami menggigil?"),
    ("tidak_enak_badan", "Apakah Anda merasa tidak enak badan?"),
    ("demam", "Apakah Anda mengalami demam?"),
    ("keringat_dingin", "Apakah Anda mengalami keringat dingin?"),
    ("sakit_kepala", "Apakah Anda mengalami sakit kepala?"),
    ("mimisan", "Apakah Anda mengalami mimisan?"),
    ("mual", "Apakah Anda mengalami mual?")
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Malaria")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar", font=("Arial", 12))
        self.label_tanya.pack(pady=20)
        
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, command=lambda: self.jawab('t'))
        
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil_diagnosa = []
        for penyakit, gejala in database_penyakit.items():
            if all(s in self.gejala_terpilih for s in gejala):
                hasil_diagnosa.append(penyakit)

        if hasil_diagnosa:
            kesimpulan = "Anda kemungkinan terjangkit:\n" + "\n".join(hasil_diagnosa)
        else:
            kesimpulan = "Tidak ditemukan kecocokan dengan penyakit Malaria pada sistem."
        
        messagebox.showinfo("Hasil Diagnosa", kesimpulan)
        
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x250")
    app = AplikasiPakar(root)
    root.mainloop()