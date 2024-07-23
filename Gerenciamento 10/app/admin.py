from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .models import CustomUser

admin.site.register(Produto)
admin.site.register(DetalheProduto)
admin.site.register(TipoEmbalagem)
admin.site.register(Modelo)
admin.site.register(Fabricante)
admin.site.register(Marca)
admin.site.register(Instituic)
admin.site.register(InstituicUnidade)
admin.site.register(SectorSuper)
admin.site.register(Sector)
admin.site.register(Subsector)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Transaction)
admin.site.register(UnidadeMedida)
admin.site.register(Tipo)
admin.site.register(Subtipo)
admin.site.register(MovimentacaoProduto)
admin.site.register(ProdutoMovimentoItem)


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'subsetor', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'subsetor')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'subsetor')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'subsetor'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
