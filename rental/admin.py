from django.contrib import admin
from .models import Merek, Motor, Peminjaman


@admin.register(Merek)
class MerekAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi')
    search_fields = ('nama',)


@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    list_display = ('nama', 'merek', 'nomor_polisi', 'harga_per_hari', 'status')  # Tambahkan 'status'
    search_fields = ('nama', 'nomor_polisi')
    list_filter = ('merek', 'status')  # Filter berdasarkan status
    list_per_page = 10



@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    list_display = (
        'nama_peminjam', 
        'motor', 
        'tanggal_pinjam', 
        'tanggal_kembali', 
        'jumlah_bayar', 
        'sudah_bayar', 
        'status'
    )
    search_fields = ('nama_peminjam', 'motor__nama')
    list_filter = ('status', 'sudah_bayar')
    list_per_page = 10
    actions = ['selesaikan_peminjaman']

    def selesaikan_peminjaman(self, request, queryset):
        """
        Aksi untuk menyelesaikan peminjaman.
        """
        for peminjaman in queryset:
            peminjaman.status = 'Selesai'
            peminjaman.save()

            # Perbarui status motor menjadi 'Tersedia'
            motor = peminjaman.motor
            motor.status = 'Tersedia'
            motor.save()

        self.message_user(request, f"{queryset.count()} peminjaman telah diselesaikan.")

    selesaikan_peminjaman.short_description = "Tandai sebagai selesai"
