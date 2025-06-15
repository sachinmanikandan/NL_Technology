from . import views
from django.urls import path




urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),



    path('methods/', views.MethodListView.as_view(), name='method-list'),
    path('methods/<int:pk>/edit/', views.MethodUpdateView.as_view(), name='method-edit'),
    path('methods/<int:pk>/delete/', views.MethodDeleteView.as_view(), name='method-delete'),
    path('methods/add/', views.MethodCreateView.as_view(), name='add-method'),



    path('machines/', views.MachineListView.as_view(), name='machine-list'),
    path('machines/add/', views.MachineCreateView.as_view(), name='machine-add'),
    path('machines/<int:pk>/edit/', views.MachineUpdateView.as_view(), name='machine-edit'),
    path('machines/<int:pk>/delete/', views.MachineDeleteView.as_view(), name='machine-delete'),



    path("materials/", views.MaterialListView.as_view(), name="material-list"),
    path("materials/add/", views.MaterialCreateView.as_view(), name="material-add"),
    path("materials/<int:pk>/edit/", views.MaterialUpdateView.as_view(), name="material-edit"),
    path("materials/<int:pk>/delete/", views.MaterialDeleteView.as_view(), name="material-delete"),


    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),








  

]
