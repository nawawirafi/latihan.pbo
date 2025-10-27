class Manusia(object):
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} makan nasi")


class ManusiaMilenial(Manusia):
    def __init__(self, nama, email=None):
        super().__init__(nama)
        self.email = email

    def set_email(self, email):
        self.email = email


# Contoh penggunaan
programmer = ManusiaMilenial('Eka')
programmer.set_email('eka@test.com')
programmer.makan()

petani = ManusiaMilenial('Putra')
petani.set_email('putra@test.com')
petani.makan()
