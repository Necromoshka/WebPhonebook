from django.forms import ModelForm


from .models import Person



class PrForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'surnsurnameame', 'patronymic', 'mob_tel_num', 'em', 'subdivision', 'extension')
