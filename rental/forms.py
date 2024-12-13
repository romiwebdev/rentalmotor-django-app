from django import forms
from .models import Peminjaman


class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ['nik', 'nama_peminjam', 'tanggal_pinjam', 'tanggal_kembali']
        widgets = {
            'tanggal_pinjam': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_kembali': forms.DateInput(attrs={'type': 'date'}),
        }
