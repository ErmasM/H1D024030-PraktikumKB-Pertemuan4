import tkinter as tk
from tkinter import messagebox

database_kerusakan = {
    "Baterai Rusak / Bocor": ["baterai_drop", "mati_sendiri", "baterai_gembung"],
    "Konektor / IC Cas Rusak": ["cas_lambat", "port_longgar", "tidak_konek_pc"],
    "Layar / LCD Bermasalah": ["ghost_touch", "layar_bergaris", "touch_tidak_respon"],
    "Sistem Operasi Bootloop": ["stuck_logo", "sering_restart", "aplikasi_error"],
    "Modul Kamera Rusak": ["kamera_buram", "kamera_blank", "flash_mati"]
}

solusi_kerusakan = {
    "Baterai Rusak / Bocor": "Segera ganti baterai dengan yang baru/original. Bahaya jika baterai sudah kembung.",
    "Konektor / IC Cas Rusak": "Bersihkan port charger pakai jarum/sikat. Jika masih error, bawa ke teknisi untuk ganti papan konektor (konektor cas).",
    "Layar / LCD Bermasalah": "Kemungkinan besar panel LCD atau kabel fleksibel rusak. Perlu diganti satu set LCD baru.",
    "Sistem Operasi Bootloop": "Coba lakukan Factory Reset via Recovery Mode. Jika masih mentok logo, HP perlu di-flash ulang (install ulang OS).",
    "Modul Kamera Rusak": "Bersihkan kaca kamera luar. Jika masih blank atau tidak fokus, modul kamera di dalam mesin perlu diganti."
}

semua_gejala = [
    ("baterai_drop", "Apakah persentase baterai berkurang drastis secara tiba-tiba?"),
    ("mati_sendiri", "Apakah HP sering mati sendiri padahal baterai masih di atas 20%?"),
    ("baterai_gembung", "Apakah bodi belakang/layar HP terlihat sedikit terangkat (kembung)?"),
    ("cas_lambat", "Apakah pengisian daya terasa sangat lambat atau persentase tidak nambah?"),
    ("port_longgar", "Apakah kabel charger terasa sangat longgar saat dicolokkan ke HP?"),
    ("tidak_konek_pc", "Apakah HP tidak terdeteksi sama sekali saat disambung ke laptop?"),
    ("ghost_touch", "Apakah layar sering bergerak atau menekan sendiri tanpa disentuh?"),
    ("layar_bergaris", "Apakah muncul tompel hitam, garis, atau layar sering berkedip?"),
    ("touch_tidak_respon", "Apakah sebagian atau seluruh layar tidak merespon saat disentuh?"),
    ("stuck_logo", "Apakah HP hanya mentok di logo merk terus-menerus saat dinyalakan?"),
    ("sering_restart", "Apakah HP sering mati dan menyala kembali dengan sendirinya?"),
    ("aplikasi_error", "Apakah sering muncul tulisan 'Aplikasi telah berhenti' (Force Close)?"),
    ("kamera_buram", "Apakah hasil foto terlihat sangat buram atau lensa tidak bisa fokus?"),
    ("kamera_blank", "Apakah aplikasi kamera menampilkan layar hitam (blank) saat dibuka?"),
    ("flash_mati", "Apakah lampu flash/senter mati dan tidak bisa dinyalakan?")
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa HP")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya = tk.Label(root, text="Sistem Diagnosa Kerusakan Smartphone", font=("Arial", 12))
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
        
        for kerusakan, gejala in database_kerusakan.items():
            gejala_cocok = sum(1 for s in gejala if s in self.gejala_terpilih)
            if gejala_cocok >= 2: 
                hasil_diagnosa.append(kerusakan)

        if hasil_diagnosa:
            kesimpulan = "HP Anda kemungkinan mengalami:\n\n"
            for k in hasil_diagnosa:
                kesimpulan += f"[{k}]\nSolusi: {solusi_kerusakan[k]}\n\n"
        else:
            kesimpulan = "Tidak ditemukan kecocokan kerusakan pada sistem kami.\nCoba periksa kembali gejalanya."
        
        messagebox.showinfo("Hasil Diagnosa", kesimpulan)
        
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("550x250")
    app = AplikasiPakar(root)
    root.mainloop()