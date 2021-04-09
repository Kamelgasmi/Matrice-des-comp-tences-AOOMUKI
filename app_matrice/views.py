from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
# from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import AddUserForm, AddCollaboraterForm, AddFieldForm, AddCompetenceForm, AddCertificationForm, AddSocietyForm, ProfilForm, ModifyProfilForm, AddCompCollabForm, AddSocietyForm, ProfilFormUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# class UserList(ListView):
  
#     # specify the model for list view
#     model = User
#     template_name = 'User_List.html'
    
def index(request):
    # users = User.objects.all()
    # context = { 'users':users}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))

#*************************************************************************************************************
def ListUsers(request):
    profil = Profil.objects.all()
    profiluser = ProfilUser.objects.all()
    collaborater = Collaborater.objects.all()
    users = User.objects.all()
    context = {
        'profiluser':profiluser,
        'profil': profil,
        'users': users,
        'collaborater': collaborater,
    }
    return render(request, 'app/User_List.html', context)

def DeleteUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user_id': user.id,
    }
    user.delete()
    messages.success(request, "L'utilisateur a été supprimé")
    return redirect('matrice:Liste_des_utilisateurs')

#*************************************************************************************************************

def ListCollaboraters(request):
    collaborater = Collaborater.objects.all().order_by('collaborater') #.order_by('Society')
    profil = Profil.objects.all()
    society = Society.objects.all()
    context = {
        'collaborater': collaborater,
        'profil': profil,
        'society': society,
    }
    return render(request, 'app/Collaboraters_List.html', context)

def DeleteCollab(request, collaborater_id):
    collab = get_object_or_404(Collaborater, pk=collaborater_id)
    context = {
        'collab': collab,
    }
    collab.delete()
    messages.success(request, "Le collaborateur a été supprimé")
    return redirect('matrice:Liste_des_collaborateurs')

#*************************************************************************************************************

def Profils(request, collaborater_id):
    user=User.objects.all()
    collaborater = get_object_or_404(Collaborater, pk=collaborater_id)
    # field=Field.objects.all()
    profil = Profil.objects.all()
    # listcompetence = ListofCompetence.objects.all()
    # competence=Competence.objects.all()
    context = {
        'profil':profil,
        # 'field':field,
        # 'listcompetence':listcompetence,
        # 'competence':competence,
        'collaborater':collaborater,
        'user':user,
    }
    return render(request, 'app/Profil.html', context)

# @login_required
def CollaboraterProfil(request, user_id):
    profiluser = ProfilUser.objects.all()
    user=get_object_or_404(User,pk=user_id)
    collaborater = Collaborater.objects.all()
    profil = Profil.objects.all()
    field=Field.objects.all()
    listcompetence = ListofCompetence.objects.all()
    competence=Competence.objects.all()
    # level=ListLevel.objects.all()
    # interest=ListInterest.objects.all()
    # qs = user.app_set.all()
    context = {
        'profiluser':profiluser,
        'user':user,
        'collaborater':collaborater,
        'profil':profil,
        'field':field,
        'listcompetence':listcompetence,
        'competence':competence,
        # 'level':level,
        # 'interest':interest,
        # 'qs':qs
    }
    return render(request, 'app/profilCollaborater.html', context)


# def search(request):
#     query = request.GET.get('query')
#     if not query:
#         collaborater = Collaborater.objects.all()
#     else:
#         collaborater = Collaborater.objects.filter(Lastname__icontains=query)
#     if not collaborater.exists():
#         collaborater = Collaborater.objects.filter(Society__icontains=query)
#     title = "Résultats pour la requête %s"%query
#     context = {
#         'collaborater': collaborater,
#         # 'name': name,
#     }
#     return render(request, 'app/search.html', context)

def ListOfCertification(request):
    certification=ListCertification.objects.all()
    context = {
        'certification': certification,
    }
    return render(request, 'app/Certification_List.html', context)

def ListSociety(request):
    society=Society.objects.all()
    context = {
        'society': society,
    }
    return render(request, 'app/Society_List.html', context)

def ListField(request):
    field=Field.objects.all()
    context = {
        'field': field,
    }
    return render(request, 'app/Field_List.html', context)

def ListCompetence(request):
    competence=Competence.objects.all()
    field=Field.objects.all()
    context = {
        'competence': competence,
        'field': field,

    }
    return render(request, 'app/Competence_List.html', context)

def register(request):
    collaborater = Collaborater.objects.all()
    form6 = AddCollaboraterForm()
    form = AddUserForm()
    context = {
        'collaborater': collaborater,
        'form6': form6,
        'form': form,
    }
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        form6 = AddCollaboraterForm(request.POST)
        if form.is_valid() and form6.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            collab = form6.save(commit=False)
            collab.user = user
            collab.save()
            messages.success(request,f'Bienvenue {username}, votre compte a été crée avec succés')
            return redirect('matrice:Liste_des_utilisateurs')
        else:
            messages.error(request, "Vous avez déjà un compte")
    else:
        form = AddUserForm()
        form6 = AddCollaboraterForm()
    return render(request, 'registration/register.html', context)

def AddFieldCompDegreeSociety(request):
    field=Field.objects.all()
    competence=Competence.objects.all()
    context = {
        'field': field,
        'competence': competence,
    }
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = AddFieldForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            field = Field.objects.filter(name=name)
            if not field.exists():
                form1.save()
                messages.success(request, f' Le domaine {name} a été ajouté')
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return redirect('matrice:Liste_des_domaines')

    elif request.method == 'POST' and 'btnform2' in request.POST:
        form2 = AddCompetenceForm(request.POST)
        if form2.is_valid():
            name = form2.cleaned_data['name']
            competence = Competence.objects.filter(name=name)
            if not competence.exists():
                form2.save()
                messages.success(request, f' La compétence {name} a été ajoutée')
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return redirect('matrice:Liste_des_compétences')

    elif request.method == 'POST' and 'btnform3' in request.POST:
        form3 = AddCertificationForm(request.POST)
        if form3.is_valid():
            name = form3.cleaned_data['name']
            certification = ListCertification.objects.filter(name=name)
            if not certification.exists():
                form3.save()
                messages.success(request, f' La certification {name} a été ajoutée')
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return redirect('matrice:Liste_des_certifications')

    elif request.method == 'POST' and 'btnform4' in request.POST:
        form4 = AddSocietyForm(request.POST)
        if form4.is_valid():
            name = form4.cleaned_data['name']
            society = Society.objects.filter(name=name)
            if not society.exists():
                form4.save()
                messages.success(request, f' La société {name} a été ajoutée')
                form1 = AddFieldForm()
                form2 = AddCompetenceForm()
                form3 = AddCertificationForm()
                form4 = AddSocietyForm()
            return redirect('matrice:Liste_des_sociétés')

    else:
        form1 = AddFieldForm()
        form2 = AddCompetenceForm()
        form3 = AddCertificationForm()
        form4 = AddSocietyForm()
    return render(request, 'app/AddFieldCompetence.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})

def AddInfoCollab(request, user_id):
    profil = Profil.objects.all()
    profiluser = ProfilUser.objects.all()
    user = get_object_or_404(User,pk=user_id)
    collaborater = Collaborater.objects.all()
    form = ProfilForm()
    form1 = ProfilFormUser()
    # form5 = CollaboraterForm()
    context = {
        'user': user,
        'profil': profil,
        'profiluser': profiluser,
        'form': form,
        'collaborater': collaborater,
        'form1': form1,

        # 'form5': form5
    }
    if request.method == 'POST' and 'btnform2' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form = ProfilForm(request.POST)
            if form.is_valid():
                society = form.cleaned_data['society']
                Extern = form.cleaned_data['Extern']
                workstation = form.cleaned_data['workstation']
                profil = Profil.objects.filter(user=user_id)
                if not profil.exists():
                    formComp1 = form.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                    formComp1.user = User.objects.get(pk=request.user.id) 
                    formComp1.save() # sauvergarde tout cette fois ci
                    form.save_m2m()#sauvergarde le champs manytomany
                    messages.success(request, "Vos informations ont été ajoutées.")
                    return render(request, 'app/formInformationCollab.html', context)
                else:
                    messages.error(request, "Vous avaez déja enregistré vos informations ")
                    
    elif request.method == 'POST' and 'btnform1' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form1 = ProfilFormUser(request.POST)
            if form1.is_valid():
                # society = form.cleaned_data['society']
                profiluser = ProfilUser.objects.filter(user=user_id)
                if not profiluser.exists():
                    formComp2 = form1.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                    formComp2.user = User.objects.get(pk=request.user.id) 
                    formComp2.save() # sauvergarde tout cette fois ci
                    messages.success(request, "Vos informations ont été ajoutées.")
                    return render(request, 'app/formInformationCollab.html', context)
                else:
                    messages.error(request, "Vous avez déja enregistré vos informations ")
    else:
        form = ProfilForm()
        form1 = ProfilFormUser()
        # form5 = CollaboraterForm()
        context = {
        'user': user,
        'profil': profil,
        'profiluser': profiluser,
        'form': form,
        'form1': form1,
        'collaborater': collaborater,
        # 'form5': form5
        }
    return render(request, 'app/FormInformationCollab.html', context)

def ModifyInfoCollab(request, profil_id, ):
    profil = get_object_or_404(Profil,pk=profil_id)
    form = ModifyProfilForm(instance=profil)
    context = {
        'profil': profil,
        'form': form

    }
    if request.method == 'POST' and 'btnform2' in request.POST : #and request.is_ajax
        if request.user.is_authenticated:
            form = ModifyProfilForm(request.POST, instance=profil)
            if form.is_valid():
                society = form.cleaned_data['society']
                Extern = form.cleaned_data['Extern']
                workstation = form.cleaned_data['workstation']
                formComp2 = form.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                formComp2.save() # sauvergarde tout cette fois ci
                form.save_m2m()#sauvergarde le champs manytomany
                # data = {
                # 'message':'form is saved'
                # }
                # return JsonResponse(data)
                messages.success(request, "Vos informations ont été modifiées")
                form = ModifyProfilForm()
                return render(request, 'app/FormModifyInfoCollab.html', context)
    else:
        form3 = ModifyProfilForm(instance=profil)
        context = {
        'profil': profil,
        'form': form
        }
    return render(request, 'app/FormModifyInfoCollab.html', context)

def AddCompetenceCollab(request, user_id):
    profil = Profil.objects.all()
    collaborater = Collaborater.objects.all()
    certification = ListCertification.objects.all()
    user = get_object_or_404(User,pk=user_id)
    listcompetence = ListofCompetence.objects.all()
    competence = Competence.objects.all()
    form = AddCompCollabForm()
    context = {
        'user': user,
        'profil': profil,
        'listcompetence': listcompetence,
        'form': form,
        'collaborater': collaborater,
    }
    if request.method == 'POST' and 'btnform1' in request.POST: #and request.is_ajax
        if request.user.is_authenticated:
            form = AddCompCollabForm(request.POST)
            if form.is_valid():
                interest = form.cleaned_data['Interest']
                level = form.cleaned_data['Level']
                competence = form.cleaned_data['Competence']
                listcomp = ListofCompetence.objects.filter(User_id=user_id, Competence=competence)
                if not listcomp.exists():
                    formComp = form.save(commit=False) # Renvoyer un objet sans enregistrer dans la base de données
                    formComp.User = User.objects.get(pk=request.user.id) 
                    formComp.save() # sauvergarde tout cette fois ci
                    messages.success(request, "La compétence a été ajoutée")
                    form = AddCompCollabForm()
                    return render(request, 'app/FormCompetencesCollab.html', context)
                else:
                    messages.error(request, "Vous avez déjà ajouté cette compétence")
    else:
        form = AddCompCollabForm()
        context = {
        'user': user,
        'profil': profil,
        'listcompetence': listcompetence,
        'form': form,
        'collaborater': collaborater,
        }
    return render(request, 'app/FormCompetencesCollab.html', context)

# class PasswordsChangeView(PasswordChangeView):
#     from_class = PasswordChangeForm
#     succes_url = reverse_lazy('index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user )
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Votre mot de passe a été mis à jour')
            return redirect('matrice:change_password')
        else:
            messages.error(request, 'Veuillez entrer un mot de passe valide')
            return redirect('matrice:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form })
    
# def AddCollabForm(request):
#     collaborater = Collaborater.objects.all()
#     form6 = AddCollaboraterForm()
#     context = {
#         'collaborater': collaborater,
#         'form6': form6,
#     }
#     if request.method == 'POST' and 'btnform1' in request.POST:
#         form6 = AddCollaboraterForm(request.POST)
#         if form6.is_valid():
#             collaborater = form6.cleaned_data['collaborater']
#             user = form6.cleaned_data['user']
#             collaborater = Collaborater.objects.filter(user=user)
#             if not collaborater.exists():
#                 form6.save()
#                 messages.success(request, "Le collaborater a été ajouté")
#                 form6 = AddCollaboraterForm()
#                 return render(request, 'registration/AddCollab.html', context)
#             else:
#                 messages.error(request, "Ce collaborateur existe déjà")
#     else:
#         form6 = AddCollaboraterForm()
#         context = {
#             'collaborater': collaborater,
#             'form6': form6,
#         }
#     return render(request, 'registration/AddCollab.html', context)
