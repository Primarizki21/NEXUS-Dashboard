# Panduan Kolaborasi (Contributing Guidelines)

Repositori ini menggunakan alur kerja berbasis **Feature Branch & Pull Request**. Semua kontributor dan kolaborator **dilarang melakukan commit atau push langsung ke branch `main`**.

---

## 1. Setup Awal (Wajib Setelah Clone)

Aktifkan git hook bawaan repositori agar terlindung dari salah commit ke `main`:

```bash
git config core.hooksPath .githooks
```

Setelah perintah ini dijalankan, git akan otomatis menolak jika kamu tidak sengaja mencoba commit atau push langsung ke branch `main`.

---

## 2. Alur Pengerjaan Fitur / Analisis

### Langkah 1: Sinkronkan branch `main` terbaru
```bash
git checkout main
git pull origin main
```

### Langkah 2: Buat branch baru dari `main`
Gunakan konvensi penamaan branch yang jelas:
* `feat/<nama-fitur>`: Penambahan analisis baru, notebook, visualisasi, atau data.
* `fix/<nama-perbaikan>`: Perbaikan kalkulasi atau bug skrip.
* `docs/<nama-dokumen>`: Pembaruan draf laporan, template masalah, atau ringkasan temuan.

Contoh:
```bash
git checkout -b feat/analisis-spasial
```

### Langkah 3: Kerjakan perubahan & commit
Pastikan setiap commit bersifat atomik dan memiliki pesan deskriptif:
```bash
git add .
git commit -m "feat(spasial): tambahkan estimasi model Spatial Durbin dan matriks bobot"
```

### Langkah 4: Push branch ke remote
```bash
git push -u origin feat/analisis-spasial
```

### Langkah 5: Buat Pull Request (PR) di GitHub
1. Buka repositori di GitHub.
2. Klik tombol **Compare & pull request**.
3. Berikan deskripsi perubahan dan minta review ke rekan tim.
4. Setelah diverifikasi dan disetujui, lakukan penggabungan (*merge*) ke branch `main`.

---

## 3. Catatan Standar Format Teks
* Gunakan baris baru berformat LF (`\n`), bukan Windows CRLF (`\r\n`).
* Hindari commit file arsip biner seperti `.zip`.
