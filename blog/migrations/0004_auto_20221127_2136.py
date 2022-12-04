# Generated by Django 2.2.12 on 2022-11-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221127_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kode_Dosen', models.TextField()),
                ('Nama_Dosen', models.TextField(blank=True, null=True)),
                ('Alamat', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NPM', models.TextField()),
                ('Nama', models.TextField(blank=True, null=True)),
                ('Jurusan', models.TextField(blank=True, null=True)),
                ('Kelas', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kode_Matkul', models.TextField()),
                ('Nama_Matkul', models.TextField(blank=True, null=True)),
                ('SKS', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-world', unique=True),
            preserve_default=False,
        ),
    ]