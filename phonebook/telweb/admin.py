from django.contrib import admin

# Register your models here.
from .models import Person


class PrsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnsurnameame', 'patronymic',)
    list_display_links = ('name', 'surnsurnameame', 'patronymic',)
    search_fields = ('name', 'surnsurnameame', 'patronymic',)


admin.site.register(Person, PrsAdmin)
