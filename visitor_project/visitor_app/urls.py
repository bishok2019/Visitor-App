from django.urls import path
from . import views

urlpatterns = [
    path('get_visitor/', views.VisitorView.as_view(), name='get-visitor' ),
    path('', views.RegisterVisiterView.as_view(), name='register-visitor' ),
]