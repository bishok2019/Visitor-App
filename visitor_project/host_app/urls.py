from django.urls import path
from host_app import views

urlpatterns = [
    ####################For Host#########################
    path('register/', views.HostRegistrationView.as_view(), name='register-host' ),
    path('login/', views.HostLoginView.as_view(), name='login-host' ),
    # path('appointment/', views.YourAppointmentView.as_view(), name='your-appointment' ),
    path('appointments/<int:pk>', views.RescheduleVisitor.as_view(), name='modify-visitor-schedule-info' ),
    path('appointments/', views.RescheduleVisitor.as_view(), name='modify-visitor-schedule-info' ),
    path('info/', views.GetYourHostInfo.as_view(), name='get-host-info' ),
    ####################For Admin#########################
    path('registerdepartment/', views.DepartmentRegistrationView.as_view(), name='register-depart' ),
    path('all/', views.ListHostView.as_view(), name='get-all-host' ),
    path('modify/<int:pk>', views.ModifyHostView.as_view(), name='modify-host' ),
]