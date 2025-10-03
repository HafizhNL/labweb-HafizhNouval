from django.urls import path
from . import views

urlpatterns = [
    path('promotion', views.Promotion, name='promotion'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('home', views.Home, name='home'),
    path('lowongan', views.Konfirm, name='lowongan'),
    path('kaprodi', views.Kaprodi, name='kaprodi'),
    path('laporan_kemajuan', views.UTS, name='laporan_kemajuan'),
    path('laporan_kemajuan/<int:laporan_id>/', views.UTSDetail, name='laporan_kemajuan_detail'),
    path('laporan_akhir', views.UAS, name='laporan_akhir'),
    path('sertifikat', views.Sertifikat, name='sertifikat')
]