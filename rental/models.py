from django.db import models
from django.utils.timezone import now


class Merek(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama


class Motor(models.Model):
    STATUS_CHOICES = [
        ('Tersedia', 'Tersedia'),
        ('Dipinjam', 'Dipinjam'),
    ]
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE)
    nomor_polisi = models.CharField(max_length=20, unique=True)
    harga_per_hari = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='motor_images/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Tersedia')  # Kolom baru

    def __str__(self):
        return f"{self.nama} - {self.nomor_polisi}"



class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('In Use', 'In Use'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    nik = models.CharField(max_length=16)
    nama_peminjam = models.CharField(max_length=100)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    nomor_polisi = models.CharField(max_length=50)
    tanggal_pinjam = models.DateField(default=now)
    tanggal_kembali = models.DateField()
    jumlah_bayar = models.DecimalField(max_digits=10, decimal_places=2)
    sudah_bayar = models.BooleanField(default=False)
    jumlah_denda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')

    def __str__(self):
        return f"{self.nama_peminjam} - {self.motor.nama} ({self.status})"
