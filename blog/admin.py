from django.contrib import admin

# Register your models here.
from .models import (BlogPost, Mahasiswa, Dosen, Matakuliah)

admin.site.register(BlogPost)
admin.site.register(Mahasiswa)
admin.site.register(Dosen)
admin.site.register(Matakuliah)
