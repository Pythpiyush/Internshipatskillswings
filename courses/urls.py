from courses import views
from django.urls import path, include

urlpatterns = [
    path('ielts/', include('ielts.urls')),
    path('', views.home, name='home'),
]
