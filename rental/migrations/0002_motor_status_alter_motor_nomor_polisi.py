# Generated by Django 5.1.3 on 2024-11-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor',
            name='status',
            field=models.CharField(choices=[('Tersedia', 'Tersedia'), ('Dipinjam', 'Dipinjam')], default='Tersedia', max_length=10),
        ),
        migrations.AlterField(
            model_name='motor',
            name='nomor_polisi',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
