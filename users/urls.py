from django.urls import path
from users.views import (log_in)

app_name = 'users'
urlpatterns = {
    path('login/', log_in, name='login')
}