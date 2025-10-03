from django.contrib import admin
from .models import Mahasiswa, Lowongan, LaporanKemajuan, LaporanAkhir

# Register your models here.
admin.site.register(Mahasiswa)
admin.site.register(Lowongan)
admin.site.register(LaporanKemajuan)
admin.site.register(LaporanAkhir)