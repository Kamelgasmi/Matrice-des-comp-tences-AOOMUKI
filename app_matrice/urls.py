from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'matrice'

urlpatterns = [
    path('Connexion/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='Connexion'),
    path('Deconnexion/', auth_views.LogoutView.as_view(next_page='matrice:Connexion',template_name='registration/logout.html'), name='Deconnexion'),
    path('', views.index, name='index'),
    # path('search/', views.search, name='search'),
    re_path(r'^(?P<collaborater_id>[0-9]+)/$', views.Profils, name='Profils'),
    path('Liste_des_utilisateurs/', views.ListUsers, name='Liste_des_utilisateurs'),
    re_path(r'^DeleteUser/(?P<user_id>[0-9]+)/$', views.DeleteUser, name='DeleteUser'),
    path('Liste_des_collaborateurs/', views.ListCollaboraters, name='Liste_des_collaborateurs'),
    re_path(r'^DeleteCollab/(?P<collaborater_id>[0-9]+)/$', views.DeleteCollab, name='DeleteCollab'),
    path('Liste_des_certifications/', views.ListOfCertification, name='Liste_des_certifications'),
    path('Liste_des_sociétés/', views.ListSociety, name='Liste_des_sociétés'),
    path('Liste_des_domaines/', views.ListField, name='Liste_des_domaines'),
    path('Liste_des_compétences/', views.ListCompetence, name='Liste_des_compétences'),
    path('Enregistrement/', views.register, name='Enregistrement'),
    path('Ajouter_Domaines_Compétences/', views.AddFieldCompDegreeSociety, name='Ajouter_Domaines_Compétences'),
    re_path(r'^Mon_profil/(?P<user_id>[0-9]+)/$', views.CollaboraterProfil, name='Mon_profil'),




    # path('Ajouter_Domaines_Compétences/', views.AddFieldCompDegreeSociety, name='Ajouter_Domaines_Compétences'),

]