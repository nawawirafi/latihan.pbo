class Kendaraan(object):
    def __init__(self, nama):
        self.nama = nama

    def jalan(self):
        print(f"{self.nama} sedang berjalan di jalan raya.")


class KendaraanModern(Kendaraan):
    def __init__(self, nama, fitur=None):
        super().__init__(nama)
        self.fitur = fitur

    def set_fitur(self, fitur):
        self.fitur = fitur

    def tampilkan_fitur(self):
        print(f"{self.nama} memiliki fitur modern: {self.fitur}")


# Contoh penggunaan
mobil = KendaraanModern('Honda Supra')
mobil.set_fitur('Sistem GPS & Sensor Parkir')
mobil.jalan()
mobil.tampilkan_fitur()

motor = KendaraanModern('Toyota Supra')
motor.set_fitur('Quick Shifter & Mode Balap')
motor.jalan()
motor.tampilkan_fitur()
