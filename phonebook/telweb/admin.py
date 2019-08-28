from django.contrib import admin

# Register your models here.
from .models import Person, InTel,Cabinet, Organization


class PrsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnsurnameame', 'patronymic', 'extension',)
    list_display_links = ('name', 'surnsurnameame', 'patronymic',)
    search_fields = ('name', 'surnsurnameame', 'patronymic',)


admin.site.register(Person, PrsAdmin)
admin.site.register(InTel)
admin.site.register(Cabinet)
admin.site.register(Organization)
