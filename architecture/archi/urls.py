from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('ajout/',views.ajout, name="Ajout"),
    path('traitement/',views.traitement, name="Traitement"),
    path('update_oeuvre/<int:id>/',views.update_oeuvre, name="Upoeuvre"),
    path('delete/<int:id>/', views.delete, name="Delete"),
    path('liste_oeuvre/',views.liste_oeuvre, name="Lioeuvre"),


    path('ajout_architecte/', views.ajout_architecte, name="Ajarchi"),
    path('liste_architecte/', views.liste_architecte, name="Architecte"),
    path('update_architecte/<architecte_id>', views.update_architecte, name="Uparchi"),
    path('delete_architecte/<architecte_id>,', views.delete_architecte, name="Delarchi"),

    path('search/', views.search, name="Search"),

]