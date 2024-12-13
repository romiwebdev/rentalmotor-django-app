from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Motor
from .forms import PeminjamanForm


def home(request):
    # Ambil semua motor yang ada di database
    motors = Motor.objects.all()
    context = {'motors': motors}
    return render(request, 'home.html', context)

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Motor
from .forms import PeminjamanForm

def motor_detail(request, motor_id):  # Gunakan motor_id sebagai parameter
    """
    Menampilkan detail motor tertentu dan formulir untuk memesan peminjaman.
    """
    motor = get_object_or_404(Motor, id=motor_id)  # Mengambil motor berdasarkan motor_id
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            peminjaman = form.save(commit=False)
            peminjaman.motor = motor
            peminjaman.nomor_polisi = motor.nomor_polisi
            peminjaman.jumlah_bayar = (
                (peminjaman.tanggal_kembali - peminjaman.tanggal_pinjam).days
                * motor.harga_per_hari
            )
            peminjaman.save()

            # Perbarui status motor menjadi 'Dipinjam'
            motor.status = 'Dipinjam'
            motor.save()

            return redirect('rental:home')
    else:
        form = PeminjamanForm()

    context = {'motor': motor, 'form': form}
    return render(request, 'motor_detail.html', context)
