from django.urls import path
from host_app import views

urlpatterns = [
    path('register/', views.HostRegistrationView.as_view(), name='register-host' ),
    path('registerdepartment/', views.DepartmentRegistrationView.as_view(), name='register-depart' ),
    path('login/', views.LoginView.as_view(), name='login-host' ),
    path('modify/<int:pk>', views.ModifyHostView.as_view(), name='modify-host' ),
]