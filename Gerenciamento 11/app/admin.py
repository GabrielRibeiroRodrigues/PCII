from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .models import CustomUser


class DetalheProdutoEstoqueInline(admin.TabularInline):
    model = DetalheProdutoEstoque
    extra = 1

class DetalheProdutoAdmin(admin.ModelAdmin):
    inlines = [DetalheProdutoEstoqueInline]
    
admin.site.register(DetalheProduto, DetalheProdutoAdmin)
admin.site.register(DetalheProdutoEstoque)

class SubsectorInline(admin.TabularInline):
    model = Subsector
    extra = 1

class SectorAdmin(admin.ModelAdmin):
    inlines = [SubsectorInline]
    
admin.site.register(Sector, SectorAdmin)
admin.site.register(Subsector)

class InstituicUInline(admin.TabularInline):
    model = InstituicUnidade
    extra = 1

class InstituicAdmin(admin.ModelAdmin):
    inlines = [InstituicUInline]
    
admin.site.register(Instituic, InstituicAdmin)
admin.site.register(InstituicUnidade)


admin.site.register(Produto)
admin.site.register(TipoEmbalagem)
admin.site.register(Modelo)
admin.site.register(Fabricante)
admin.site.register(Marca)
admin.site.register(SectorSuper)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Transaction)
admin.site.register(UnidadeMedida)
admin.site.register(Tipo)
admin.site.register(Subtipo)
admin.site.register(MovimentacaoProduto)
admin.site.register(ProdutoMovimentoItem)
admin.site.register(DetalheProdutoFoto)
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
