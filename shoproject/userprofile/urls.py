from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),

]

