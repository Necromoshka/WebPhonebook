from django.shortcuts import render
#from django.http import HttpResponse
from .models import Person, InTel
#from django.template import loader

# Create your views here.
def index(request):
 #   template = loader.get_template('telweb/index.html')
    prs = Person.objects.all()
    #context = {'prs' : prs}
    #s = 'Список телефонов\r\n\r\n\r\n'
    #for Pr in Person.objects.order_by('subdivision'):
    #    s += Pr.name + '\r\n' + Pr.surnsurnameame + '\r\n' + Pr.patronymic +  '\r\n' + Pr.mob_tel_num + '\r\n' + Pr.em + '\r\n\r\n'
    return render(request, 'telweb/index.html', {'prs' : prs})#HttpResponse(template.render(context, request))                            #s, content_type='text/plain; charset=utf-8')

def by_intel(request, telnum):
    in_t = InTel.objects.filter(tel=telnum)
    prs = Person.objects.filter(extension=in_t[0])
    return render(request, 'telweb/cur_tel.html', {'prs':prs})
