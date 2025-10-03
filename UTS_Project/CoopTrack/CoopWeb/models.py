from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=50)
    angkatan = models.IntegerField()
    jenis_kelamin = models.CharField(max_length=10)
    email_outlook = models.EmailField()
    password = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    bukti_konsultasi = models.FileField(upload_to='bukti_konsultasi/')
    sptjm = models.FileField(upload_to='sptjm/')
    protofolio = models.FileField(upload_to='protofolio/')
    cv = models.FileField(upload_to='cv/')

class Lowongan(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='lowongans')
    periode_magang = models.CharField(max_length=50)
    posisi = models.CharField(max_length=100)
    nama_perusahaan = models.CharField(max_length=100)
    alamat_perusahaan = models.CharField(max_length=200)
    bidang_usaha_perusahaan = models.CharField(max_length=100)
    nama_supervisor = models.CharField(max_length=100)
    email_supervisor = models.EmailField()
    kontak_wa_supervisor = models.CharField(max_length=15)
    bukti_konfirmasi = models.FileField(upload_to='bukti_konfirmasi/')

class LaporanKemajuan(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='laporan_kemajuans')
    tanggal = models.DateField()
    profil_perusahaan = models.TextField()
    jobdesk = models.TextField()
    suasana_lingkungan_pekerjaan = models.TextField()
    apa_yang_didapatkan_dari_perkuliahan = models.TextField()
    apa_yang_belum_didapatkan_dalam_pembelajaran = models.TextField()

class LaporanAkhir(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='laporan_akhirs')
    pengalaman_magang = models.TextField()
    laporan_hasil_magang = models.FileField(upload_to='laporan_hasil_magang/')

class SelesaiCoop(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='selesai_coops')
    nama_mahasiswa = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    program_studi = models.CharField(max_length=50)
    nama_perusahaan = models.CharField(max_length=100)
    periode_magang = models.CharField(max_length=50)
    konversi_nilai_coop = models.CharField(max_length=50)

    def __str__(self):
        return self.mahasiswa.nama