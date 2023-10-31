from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import GeeksModel
from .forms import GeeksForm, GeeksModelForm

# Create your views here.

def geeks_view(request):
    content = GeeksModel.objects.all()
    context = {
        'content': content
    }
    return render(request, 'index.html', context=context)

def geeks_form(request):
    context = {}
    context['form'] = GeeksForm
    return render(request, 'form.html', context=context)

def geeks_modelform(request):
    if request.method == 'POST':
        form = GeeksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('geeks_view2')
        else:
            return redirect('geeks_form')
    else:
        context = {}
        context['form'] = GeeksModelForm
        return render(request, 'form.html', context=context)