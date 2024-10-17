from django.urls import path, include
from .views import index, notes, rest_days, register, create_note


urlpatterns = [
    path('', index, name='main'),
    path('rest_days/', rest_days, name='rest_days'),
    path('notes/', notes, name='notes'),
    # path('login/', register, name='register'),
    path('enter/', register, name='enter'),
    path('registration/', register, name='registration'),
    path('create_note/', create_note, name='create_note')
    # path('auth/', include('django.contrib.auth.urls'))
]  # Добавил name