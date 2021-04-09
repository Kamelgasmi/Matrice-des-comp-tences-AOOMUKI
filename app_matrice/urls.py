from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .api import UserViewSet, ProfilViewSet, FieldViewSet, CompetenceViewSet
# from .views import PasswordsChangeView
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profils', ProfilViewSet, basename='profil')  
router.register(r'fields', FieldViewSet, basename='field')
router.register(r'competences', CompetenceViewSet, basename='competence')
app_name = 'matrice'

urlpatterns = [
    path('api/', include(router.urls)),
    path('Connexion/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='Connexion'),
    path('Deconnexion/', auth_views.LogoutView.as_view(next_page='matrice:Connexion',template_name='registration/logout.html'), name='Deconnexion'),
    path('mot_de_passe/', views.change_password, name='change_password'),
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
    re_path(r'^Ajouter_des_informations_générales/(?P<user_id>[0-9]+)/$', views.AddInfoCollab, name='Ajouter_des_informations_générales'),
    # re_path(r'^Ajouter_des_informations_générales/(?P<user_id>[0-9]+)/$', views.AddInfoUser, name='Ajouter_des_informations_générales_Utilisateur'),
    re_path(r'^Modifier_des_informations/(?P<profil_id>[0-9]+)/$', views.ModifyInfoCollab, name='Modifier_des_informations'),
    re_path(r'^Ajouter_des_compétences/(?P<user_id>[0-9]+)/$', views.AddCompetenceCollab, name='Ajouter_des_compétences'),

    # path('Ajouter_Domaines_Compétences/', views.AddFieldCompDegreeSociety, name='Ajouter_Domaines_Compétences'),

]