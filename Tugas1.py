def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.40 * uas
    return nilai_akhir

def konversi_nilai(nilai_akhir):
    if nilai_akhir > 85:
        return "A"
    elif 80 < nilai_akhir <= 85:
        return "A-"
    elif 75 < nilai_akhir <= 80:
        return "B+"
    elif 70 < nilai_akhir <= 75:
        return "B"
    elif 65 < nilai_akhir <= 70:
        return "B-"
    elif 60 < nilai_akhir <= 65:
        return "C+"
    elif 55 < nilai_akhir <= 60:
        return "C"
    elif 50 < nilai_akhir <= 55:
        return "C-"
    elif 30 < nilai_akhir <= 50:
        return "D"
    else:
        return "E"

def main():
    print("Program NilaiMahasiswa")
    tugas = float(input("Masukan nilai Tugas Anda: "))
    uts = float(input("Masukan nilai UTS Anda: "))
    uas = float(input("Masukan nilai UAS Anda: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    print("Nilai akhir Anda:", nilai_akhir)
    
    nilai_huruf = konversi_nilai(nilai_akhir)
    print("Dalam huruf:", nilai_huruf)

if __name__ == "__main__":
    main()