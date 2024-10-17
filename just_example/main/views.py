from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Authorization, FormForNotes
from django.contrib.auth import authenticate, login
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Blogs
def index(request):
    return render(request, 'main/index.html')

def notes(request):
    notes = Blogs.objects.all()
    context = {'notes': notes}
    return render(request, 'main/notes.html', context=context)

def rest_days(request):
    return render(request, 'main/rest_days.html')

def register(request):
    if request.method == 'POST':
        form = Authorization(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # user = authenticate(request, username=cd['username'], password=cd['password'])
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            new_user = User(is_active=True, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = Authorization()
    return render(request, 'main/login.html', {'form': form})

def create_note(request):
    if request.method == 'POST':
        form = FormForNotes(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('Заголовок')
            preview = form.cleaned_data.get('Предпросмотр')
            content = form.cleaned_data.get('Содержание')
            published = form.cleaned_data.get('Дата публикации')
            new_note = Blogs(title=title, preview=preview, content=content, published=published)
            form.save()
            return HttpResponseRedirect(reverse('notes'))
    else:
        form = FormForNotes()
    return render(request, 'main/create_notes.html', {'form': form})