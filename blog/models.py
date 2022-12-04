from django.db import models

# Create your models here.

class BlogPost(models.Model):
  title = models.TextField()
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True, blank=True)
  
class Mahasiswa(models.Model):
  NPM = models.TextField()
  Nama = models.TextField(null=True, blank=True)
  Jurusan = models.TextField(null=True, blank=True)
  Kelas = models.TextField(null=True, blank=True)
  
class Dosen(models.Model):
  Kode_Dosen = models.TextField()
  Nama_Dosen = models.TextField(null=True, blank=True)
  Alamat = models.TextField(null=True, blank=True)
  
class Matakuliah(models.Model):
  Kode_Matkul = models.TextField()
  Nama_Matkul = models.TextField(null=True, blank=True)
  SKS = models.TextField(null=True, blank=True)



