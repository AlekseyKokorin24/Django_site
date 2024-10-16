from django.urls import path, include
from .views import index, notes, rest_days, register


urlpatterns = [
    path('', index, name='main'),
    path('rest_days/', rest_days, name='rest_days'),
    path('notes/', notes, name='notes'),
    path('login/', register, name='register'),
    # path('auth/', include('django.contrib.auth.urls'))
]  # Добавил name