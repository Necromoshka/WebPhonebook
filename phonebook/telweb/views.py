from django.shortcuts import render
#from django.http import HttpResponse
from .models import Person, InTel
#from django.template import loader

from django.views.generic.edit import CreateView
from .forms import PrForm, telForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    prs = Person.objects.all()
    context = {'prs' : prs}
    return render(request, 'telweb/index.html', context)


def by_intel(request, telnum):
    in_t = InTel.objects.filter(tel=telnum)
    prs = Person.objects.filter(extension= in_t[0])
    context = {'prs':prs, 'title':telnum}
    return render(request, 'telweb/cur_tel.html', context)



class PrCreateView(CreateView):
    template_name = 'telweb/create.html'
    form_class = PrForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prs'] = Person.objects.all()
        return context

class telCreateView(CreateView):
    template_name = 'telweb/createTel.html'
    form_class = telForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['In_tel'] = InTel.objects.all()
        return context
