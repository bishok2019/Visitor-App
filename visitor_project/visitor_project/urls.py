from django.contrib import admin
from django.urls import path, include
from visitor_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visitor_app.urls')),
    path('host/', include('host_app.urls')),

]
