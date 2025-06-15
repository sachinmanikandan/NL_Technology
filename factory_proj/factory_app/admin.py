from django.contrib import admin
from .models import Man, Machine, Material, Method, Shift, MachineUsage


# Inline MachineUsage for Machine Admin
class MachineUsageInline(admin.TabularInline):
    model = MachineUsage
    extra = 1  # Number of empty forms shown


# Customized Machine Admin
@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status')
    list_filter = ('type', 'status')
    inlines = [MachineUsageInline]


# Registering other models normally
admin.site.register(Man)
admin.site.register(Material)
admin.site.register(Method)
admin.site.register(Shift)
admin.site.register(MachineUsage)
