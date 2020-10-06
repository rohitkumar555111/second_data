from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView ,CreateView
from django.urls import reverse_lazy
from .forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from . models import Students ,Book
from .forms import BookForm
from django.views.generic.edit import UpdateView

from django.http import JsonResponse
from django.views import View
from .forms import PhotoForm
from .models import Photo , UserProfile


# Create your views here.
def index(request):
    students = Students.objects.all()
    return render(request,'newfiles/home.html',{'students':students})


def upload(request):
    if request.method=="POST":
        uploaded_file = request.FILES['doumentfile']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request , 'uploadfile.html')

'''def upload_book(request):
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'upload_book.html',{'form':form,})'''


'''def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html',{'book':book})'''

class BookListView(ListView):
    model  = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class UploadBookView(CreateView):
    model = Book
    form_class= BookForm
    template_name ='upload_book.html'
    success_url = reverse_lazy('class_book_list')

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('/data/class/books/')
##############################################################################







class BookUpdateView(UpdateView):
    model = Book
    fields = ["title",]
    template_name ='upload_book.html'
    success_url = reverse_lazy('class_book_list')

# upload multiple FileS


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
##############################################one ot onefiled


def register(request):
    if request.method =='POST':
        user_form= UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            print("user regiser succsssulyyy")

            return reverse_lazy('class_book_list')



    else:
        user_form= UserForm()
        profile_form = UserProfileForm()
        return render(request , 'data_app/register.html',{'user_form':user_form, 'profile_form':profile_form})
