import tkinter as tk: Mengimpor modul bawaan Python untuk membuka GUI dan memberikan nama alias "tk"
def prediksi_prodi(): Mendefinisikan sebuah fungsi dan mengubah teks "hasil_label" menjadi "Prediksi Prodi: Teknologi Informasi" ketika tombol diklik.
root = tk.Tk(): membuat objek jendela utama aplikasi.
root.title(...): memberikan judul jendela dengan teks "Aplikasi Prediksi Prodi Pilihan".
root.geometry("500x600"): mengatur dimensi ukuran jendela sebesar 500x600 piksel.
root.configure(bg="#ed8ec7"): mengubah warna latar belakang jendela menggunakan kode warna pink.

Judul Aplikasi ("judul"): Membuat komponen label teks dengan gaya huruf *Helvetica* ukuran 18 tebal, latar belakang warna ungu muda, teks putih, lalu menampilkannya menggunakan metode "pack(pady=20)" dengan jarak vertikal 20 piksel.
Wadah Input ("input_frame"): Membuat komponen *Frame* untuk mengelompokkan elemen-elemen input agar tersusun rapi di dalam jendela utama.

entries = []: menyiapkan *list* kosong untuk menampung kotak teks input nilai.
for i in range(10): melakukan perulangan sebanyak 10 kali untuk membuat label teks "Nilai Mata Pelajaran 1 sampai 10" dan kotak input (*Entry*) secara otomatis menggunakan pengatur letak "grid()" bersistem baris dan kolom.
entries.append(entry): memasukkan setiap kotak input yang terbuat ke dalam *list* penampung.

Tombol Hasil Prediksi ("prediksi_button"): Membuat tombol interaktif bertuliskan "Hasil Prediksi" yang dihubungkan ke fungsi "prediksi_prodi" melalui parameter "command".
Label Luaran Hasil ("hasil_label"): Membuat komponen label teks kosong berformat miring dengan latar belakang dan warna teks tertentu untuk menampilkan hasil prediksi nantinya.
root.mainloop()": Menjalankan perulangan program agar jendela aplikasi tetap terbuka dan responsif terhadap interaksi pengguna.