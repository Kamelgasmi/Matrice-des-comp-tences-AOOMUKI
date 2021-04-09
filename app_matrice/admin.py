from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ListWorkStation, ListCertification,  Society, Profil, Collaborater, Field, Competence
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
admin.site.site_header = 'Administration Matrice des compétences AOOMUKI'

# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = CustomUser
#     list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('email', 'first_name', 'last_name',)}),
#     )
#     fieldsets = UserAdmin.fieldsets
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('email', 'first_name', 'last_name', 'society')}),
#     )
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('society',)}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user','workstation','Extern' )
    search_fields = ['user__last_name']
    pass
#********************************************************************************************************************
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('field','name', )
    pass

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass

#********************************************************************************************************************
class ProfilInline(admin.TabularInline):
    model = Profil
    fieldsets = [
        (None, {'fields': ['Extern', 'society','workstation', 'user']})
        ] # list columns

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfilInline,] 
#********************************************************************************************************************
@admin.register(ListWorkStation)
class ListWorkStationAdmin(admin.ModelAdmin):
    pass

@admin.register(Collaborater)
class CollaboraterAdmin(admin.ModelAdmin):
    list_display = ('user','user_last_name','user_first_name', 'collaborater' )
    search_fields = ['user__last_name']
    def user_last_name(self, obj):
        return obj.user.last_name

    def user_first_name(self, obj):
        return obj.user.first_name

    pass

@admin.register(ListCertification)
class ListCertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    pass

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    pass

# @admin.register(ListofCompetence)
# class ListofCompetenceAdmin(admin.ModelAdmin):
#     list_display = ('User', 'Competence', 'ListLevel', 'ListInterest')
#     search_fields = ['User__username']
#     pass
