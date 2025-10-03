from unittest import loader
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Lowongan, Mahasiswa, LaporanKemajuan, LaporanAkhir

# Create your views here.
def Promotion(request):
    return render(request, 'promotion_page.html')

def Login(request):
    error = None
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'login':
            email = request.POST.get('email_outlook')
            password = request.POST.get('password')
            try:
                user = Mahasiswa.objects.get(email_outlook=email, password=password)
                request.session['mahasiswa_id'] = user.id
                return redirect('home')
            except Mahasiswa.DoesNotExist:
                return render(request, 'login_page.html', {'error': 'Email or password is incorrect'})
    return render(request, 'login_page.html', {'error': error})

def Register(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'register':
            Mahasiswa.objects.create(
                nama=request.POST.get('nama'),
                nim=request.POST.get('nim'),
                jurusan=request.POST.get('jurusan'),
                angkatan=request.POST.get('angkatan'),
                jenis_kelamin=request.POST.get('jenis_kelamin'),
                email_outlook=request.POST.get('email_outlook'),
                password=request.POST.get('password'),
                no_hp=request.POST.get('no_hp'),
                bukti_konsultasi=request.FILES.get('bukti_konsultasi'),
                sptjm=request.FILES.get('sptjm'),
                protofolio=request.FILES.get('protofolio'),
                cv=request.FILES.get('cv')
            )
            return redirect('login')
    return render(request, 'register_page.html')

def Home(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    nama = None
    if mahasiswa_id:
        mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
        nama = mahasiswa.nama
        nim = mahasiswa.nim
        jurusan = mahasiswa.jurusan
        angkatan = mahasiswa.angkatan
        jenis_kelamin = mahasiswa.jenis_kelamin
    return render(request, 'home_page.html', {'nama': nama, 'nim': nim, 'jurusan': jurusan, 'angkatan': angkatan, 'jenis_kelamin': jenis_kelamin})

def Konfirm(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'lowongan' and mahasiswa_id:
            mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
            Lowongan.objects.create(
                mahasiswa=mahasiswa,
                periode_magang=request.POST.get('periode_magang'),
                posisi=request.POST.get('posisi'),
                nama_perusahaan=request.POST.get('nama_perusahaan'),
                alamat_perusahaan=request.POST.get('alamat_perusahaan'),
                bidang_usaha_perusahaan=request.POST.get('bidang_usaha_perusahaan'),
                nama_supervisor=request.POST.get('nama_supervisor'),
                email_supervisor=request.POST.get('email_supervisor'),
                kontak_wa_supervisor=request.POST.get('kontak_wa_supervisor'),
                bukti_konfirmasi=request.FILES.get('bukti_konfirmasi')
            )
            return redirect('home')
    return render(request, 'lowongan_page.html')

def Kaprodi(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
    nama = mahasiswa.nama
    lowongan_list = Lowongan.objects.all()
    return render(request, 'kaprodi_page.html', {'lowongan_list': lowongan_list, 'nama': nama})

def UTS(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'laporan' and mahasiswa_id:
            mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
            LaporanKemajuan.objects.create(
                mahasiswa=mahasiswa,
                tanggal=request.POST.get('tanggal'),
                profil_perusahaan=request.POST.get('profil_perusahaan'),
                jobdesk=request.POST.get('jobdesk'),
                suasana_lingkungan_pekerjaan=request.POST.get('suasana_lingkungan_pekerjaan'),
                apa_yang_didapatkan_dari_perkuliahan=request.POST.get('apa_yang_didapatkan_dari_perkuliahan'),
                apa_yang_belum_didapatkan_dalam_pembelajaran=request.POST.get('apa_yang_belum_didapatkan_dalam_pembelajaran')
            )
            return redirect('laporan_kemajuan')
        
    laporan_list = LaporanKemajuan.objects.filter(mahasiswa__id=mahasiswa_id)
    laporan_terakhir = laporan_list.order_by('-tanggal').first()
    return render(request, 'laporan_kemajuan_page.html', {'laporan_list': laporan_list, 'laporan_terakhir': laporan_terakhir})

def UTSDetail(request, laporan_id):
    laporan = LaporanKemajuan.objects.get(id=laporan_id)
    return render(request, 'laporan_kemajuan_detail_page.html', {'laporan': laporan})

def UAS(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'laporan_akhir' and mahasiswa_id:
            mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
            LaporanAkhir.objects.create(
                mahasiswa=mahasiswa,
                pengalaman_magang=request.POST.get('pengalaman_magang'),
                laporan_hasil_magang=request.FILES.get('laporan_hasil_magang')
            )
    return render(request, 'laporan_akhir_page.html')

def Sertifikat(request):
    mahasiswa_id = request.session.get('mahasiswa_id')
    if mahasiswa_id:
        mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
        from datetime import date
        return render(request, 'sertificate_page.html', {
            'nama': mahasiswa.nama,
            'nim': mahasiswa.nim,
            'program_studi': mahasiswa.jurusan,
            'nama_perusahaan': mahasiswa.lowongans.last().nama_perusahaan if mahasiswa.lowongans.exists() else '',
            'periode_magang': mahasiswa.lowongans.last().periode_magang if mahasiswa.lowongans.exists() else '',
            'konversi_nilai_coop': 'A',  # Placeholder, replace with actual logic if needed
            'tanggal': date.today()
        })