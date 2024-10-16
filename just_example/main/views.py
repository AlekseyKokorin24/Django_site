from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Authorization
from django.contrib.auth import authenticate, login
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
def index(request):
    return render(request, 'main/index.html')

def notes(request):
    return render(request, 'main/notes.html')

def rest_days(request):
    return render(request, 'main/rest_days.html')

def register(request):
    if request.method == 'POST':
        form = Authorization(request.POST)
        if form.is_valid():
            print(User.objects.all())
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

# def register(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             print('Форма валидна')
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return HttpResponseRedirect(reversed('main'))
#         else:
#             print('form is`t valid')
#             print(request.POST)
#     else:   
#         # print(form.is_valid()) 
#         form = AuthenticationForm()
#     return render(request, 'main/login.html', {'form': form})
#     # return HttpResponseRedirect(reversed('main'))