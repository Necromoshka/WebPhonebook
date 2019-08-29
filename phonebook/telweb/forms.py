from django.forms import ModelForm


from .models import Person, InTel



class PrForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'surnsurnameame', 'patronymic', 'mob_tel_num', 'em', 'subdivision', 'extension')

class telForm(ModelForm):
    class Meta:
        model = InTel
        fields = ('tel', 'in_room')



