from django.shortcuts import render
from . import form
from django.http import HttpResponse
from second_app.models import user
# Create your views here.

def index(request):
    dic = {'text': 'my \b<ame is vishal \b '}
    return render(request, 'temp_1.html', dic)

def another_page(request):
    return HttpResponse('i am from another page')

def form_name(request):
    Form = form.user_form()
    if request.method=='POST':
        Form = form.user_form(request.POST)
        if Form.is_valid():
            Form.save()
            print(Form)
            return index(request)
        else:
            print('invalid')
    return render(request, 'form.html', {'form':Form})

def extend(request):
    return render(request, 'extend.html')






