from django.contrib import admin
from django.urls import path, include
from factory_app.views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/',include('api.urls')),
    path('', include('factory_app.urls')),



    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', SignUpView.as_view(), name='signup'),

    
]
