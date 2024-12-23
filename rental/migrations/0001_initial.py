# Generated by Django 5.1.3 on 2024-11-22 11:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('nomor_polisi', models.CharField(max_length=50, unique=True)),
                ('harga_per_hari', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gambar', models.ImageField(upload_to='motor_images/')),
                ('merek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.merek')),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16)),
                ('nama_peminjam', models.CharField(max_length=100)),
                ('nomor_polisi', models.CharField(max_length=50)),
                ('tanggal_pinjam', models.DateField(default=django.utils.timezone.now)),
                ('tanggal_kembali', models.DateField()),
                ('jumlah_bayar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sudah_bayar', models.BooleanField(default=False)),
                ('jumlah_denda', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('Booked', 'Booked'), ('In Use', 'In Use'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Booked', max_length=20)),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.motor')),
            ],
        ),
    ]
