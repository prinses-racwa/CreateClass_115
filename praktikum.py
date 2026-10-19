class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


try:
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    pp = PersegiPanjang(p, l)
    print(pp)
    print("Luas:", pp.hitung_luas())
    print("Keliling:", pp.hitung_keliling())
except ValueError:
    print("Input tidak valid dan harus berupa angka!")