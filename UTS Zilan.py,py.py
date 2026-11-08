# ==============================================================
# UTS IFE106 - Pengantar Pemrograman
# Studi Kasus : Program Pengelolaan Stok Barang
# Pengguna    : Pemilik / petugas gudang toko
# Fungsi      : Menghitung stok akhir berdasarkan barang masuk dan barang keluar, lalu menentukan status persediaan (AMAN / MENIPIS / HABIS).
# ==============================================================

print ("=" * 55)
print ("    PROGRAM PENGELOLAAN STOK BARANG")
print ("=" * 55)

# ---------- Input jumlah jenis barang (dengan validasi) ----------
while True: 
    teks = input("Jumlah jenis barang yang akan dikelola : ").strip()
    if teks.isdecimal() and int(teks) >= 1:
        jumlah_barang = int(teks)
        break
    print("   [!] Input tidak valid. Masukkan bilangan bulat minimal 1.")

# ---------- Penghitung ringkasan akhir ----------
jumlah_aman = 0
jumlah_menipis = 0
jumlah_habis = 0
total_stok_semua = 0

# ---------- Perulangan untuk setiap jenis barang ----------
for nomor in range(1, jumlah_barang + 1):
    print()
    print("-" * 55)
    print("BARANG KE-" + str(nomor))
    print("-" * 55)

    # Nama barang (tidak boleh kosong)
    while True:
        nama_barang = input("Nama barang                  : ").strip()
        if nama_barang != "":
            break
        print("   [!] Nama barang tidak boleh kosong.")

    # Stok awal (bilangan bulat >= 0)
    while True:
        teks = input("Stok awal                    : ").strip()
        if teks.isdecimal():
            stok_awal = int (teks)
            break
        print("   [!] Stok awal harus bilangan bulat >= 0.")

    # Batas stok minimum (bilangan bulat >= 0)
    while True:
        teks = input("Batas stok minimum           :").strip()
        if teks.isdecimal():
            stok_minimum = int(teks)
            break
        print("   [!] Batas minimum harus bilangan bulat >= 0.")

    stok_akhir = stok_awal
    total_masuk = 0
    total_keluar = 0

    # ---------- Perulangan pencatatan transaksi ----------
    print("Catat transaksi: M = Masuk, K = Keluar, S = Selesai")
    while True:
        jenis = input(" Jenis transaksi (M/K/S)    :").strip().upper()
        if jenis == "S":
            break
        elif jenis == "M" or jenis == "K":
            teks = input("  Jumlah                    : ").strip()
            if not teks.isdecimal() or int(teks) <= 0:
                print("  [!] Jumlah harus bilangan bulat lebih dari 0.")
                continue
            jumlah = int(teks)

            if jenis == "M":
                stok_akhir = stok_akhir + jumlah
                total_masuk = total_masuk + jumlah
                print("  -> Barang masuk dicatat. Stok sekarang:", stok_akhir)
            else:
                if jumlah > stok_akhir:
                    print("  [!] Ditolak: barang keluar (" + str(jumlah) + 
                        ") melebihi stok tersedia (" + str(stok_akhir) + ").")
                else:
                    stok_akhir = stok_akhir - jumlah
                    total_keluar = total_keluar + jumlah
                    print("  -> Barang keluar dicatat. Stok sekarang:", stok_akhir)
        else:
            print("  [!] Pilihan tidak dikenal. Gunakan M, K, S.")

    # ---------- Percabangan: menentukan status persediaan ----------
    if stok_akhir == 0:
        status = "HABIS - segera lakukan pemesanan ulang"
        jumlah_habis = jumlah_habis + 1
    elif stok_akhir <= stok_minimum:
        status = "MENIPIS - perlu segera restock"
        jumlah_menipis = jumlah_menipis + 1
    else:
        status = "AMAN"
        jumlah_aman = jumlah_aman + 1

    total_stok_semua = total_stok_semua + stok_akhir

    # ---------- Laporan per barang ----------
    print()
    print("LAPORAN STOK:", nama_barang)
    print("  Stok awal      ", stok_awal)
    print("  Total masuk    ", total_masuk)
    print("  Total keluar   ", total_keluar)
    print("  Stok akhir     ", stok_akhir, "(rumus: awal + masuk - keluar)")
    print("  Stok minimum   ", stok_minimum)
    print("  Status         ", status)

    # ---------- Ringkasan keseluruhan --------
    print()
    print("=" * 55)
    print("RINGKASAN PERSEDIAAN")
    print("=" * 55)
    print("Jumlah jenis barang :", jumlah_barang)
    print("Status AMAN         :", jumlah_aman)
    print("Status MENIPIS      :", jumlah_menipis)
    print("Status HABIS        :", jumlah_habis)
    print("Total seluruh stok  :", total_stok_semua)
    print("Terima kasih telah menggunakan program ini.")







