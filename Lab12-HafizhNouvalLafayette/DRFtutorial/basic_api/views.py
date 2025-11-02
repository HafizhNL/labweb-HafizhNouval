from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from basic_api.serializers import DRFPostSerializer, DRFPostDosenSerializer, DRFPostStudentSerializer
from basic_api.models import DRFPost, DRFDosen, DRFStudent

# Create your views here.

# API Views
class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer

class API_detail_objects(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer

class API_dosen(generics.ListCreateAPIView):
    queryset = DRFDosen.objects.all()
    serializer_class = DRFPostDosenSerializer

class API_student(generics.ListCreateAPIView):
    queryset = DRFStudent.objects.all()
    serializer_class = DRFPostStudentSerializer

class API_detail_student(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFStudent.objects.all()
    serializer_class = DRFPostStudentSerializer

# CRUD Views
def post_list(request):
    """Tampilkan semua data"""
    posts = DRFPost.objects.all()
    return render(request, 'basic_list.html', {'posts': posts})


def post_create(request):
    """Create a new post. GET -> render form, POST -> create and redirect."""
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        image = request.FILES.get('image')
        DRFPost.objects.create(name=name, author=author, rating=rating, image=image)
        return redirect('post_list')
    # GET: show simple create form
    return render(request, 'create_list.html')



def post_delete(request, pk):
    """Hapus data"""
    post = get_object_or_404(DRFPost, pk=pk)
    post.delete()
    return redirect('post_list')


def post_edit(request, pk):
    """Edit data"""
    post = get_object_or_404(DRFPost, pk=pk)
    if request.method == 'POST':
        post.name = request.POST.get('name')
        post.author = request.POST.get('author')
        post.rating = request.POST.get('rating')
        if request.FILES.get('image'):
            post.image = request.FILES['image']
        post.save()
        return redirect('post_list')
    return render(request, 'edit_list.html',{'post':post})
    

 