from django.forms import ModelForm, TextInput, EmailInput, FileInput, PasswordInput, Select, CheckboxInput,RadioSelect, CheckboxSelectMultiple
from django.forms.utils import ErrorList
from django import forms
from .models import Collaborater,Competence, Field, ListCertification, Society, Profil, ListofCompetence, ProfilUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
from django.forms import modelformset_factory
# from .models import CustomUser
# from wagtail.users.forms import UserCreationForm, UserEditForm


# class WagtailUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         widgets = {'society': forms.Select(attrs={'class': 'form-control'})}


# class WagtailUserEditForm(UserEditForm):
#     class Meta(UserEditForm.Meta):
#         model = CustomUser
#         widgets = {'society': forms.Select(attrs={'class': 'form-control'})}
        
# from .fields import GroupedModelChoiceField

# class ParagraphErrorList(ErrorList):
#     def __str__(self):
#         return self.as_divs()
#     def as_divs(self):
#         if not self: return ''
#         return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

class AddUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", 'email', 'is_superuser', 'is_staff']

class AddCollaboraterForm(forms.ModelForm):
    class Meta:
        model = Collaborater
        fields = [ "user","collaborater"]
        widgets = {
            'collaborater':CheckboxInput(attrs={'class': 'form-control'}),
            'user':Select(attrs={'class': 'form-control'}),
        }

# class AddSocietyForm(UserCreationForm):
#     class Meta:
#         model = Society
#         fields = ["name"]
#         widgets = {
#             'name':Select(attrs={'class': 'form-control'}),
#         }
        
class AddFieldForm(ModelForm):
    class Meta:
        model = Field
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

class AddCompetenceForm(ModelForm):
    class Meta:
        model = Competence
        fields = ["name", "field"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'field':Select(attrs={'class': 'form-control'}),
        }

class AddCertificationForm(ModelForm):
    class Meta:
        model = ListCertification
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

class AddSocietyForm(ModelForm):
    class Meta:
        model = Society
        fields = ["name"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }

class ProfilForm(forms.ModelForm):
    certification = forms.ModelMultipleChoiceField(queryset=ListCertification.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profil
        fields = ["society", "Extern", "workstation", "certification" ]
        widgets = {
            'society': Select(attrs={'class': 'form-control'}),
            'workstation':Select(attrs={'class': 'form-control'}),
            'Extern':CheckboxInput(attrs={'class': 'form-control'}),
        }
        
class ModifyProfilForm(forms.ModelForm):
    certification = forms.ModelMultipleChoiceField(queryset=ListCertification.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profil
        fields = ["society", "Extern", "workstation", "certification" ]
        widgets = {
            'society': Select(attrs={'class': 'form-control'}),
            'workstation':Select(attrs={'class': 'form-control'}),
            'Extern':CheckboxInput(attrs={'class': 'form-control'}),
        }

class ProfilFormUser(forms.ModelForm):
    class Meta:
        model = ProfilUser
        fields = ["society" ]
        widgets = {
            'society': Select(attrs={'class': 'form-control'}),
        }
        
# class ModifyProfilFormUser(forms.ModelForm):
#     class Meta:
#         model = Profil
#         fields = ["society" ]
#         widgets = {
#             'society': Select(attrs={'class': 'form-control'}),
#         }

class AddCompCollabForm(forms.ModelForm):
    class Meta:
        model = ListofCompetence
        fields = [ "Competence", "Interest", "Level" ]
        widgets = {
            'Competence': Select(attrs={'class': 'form-control'}),
            'Interest': Select(attrs={'class': 'form-control'}),
            'Level':Select(attrs={'class': 'form-control'}),
        }
