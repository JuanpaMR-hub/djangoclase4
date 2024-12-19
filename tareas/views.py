from django.shortcuts import render, redirect
from .forms import TareasFormExtended
from .models import Tarea
from django.contrib.auth.decorators import login_required

@login_required(login_url='usuarios:login')
def home(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TareasFormExtended(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)
        
        elif 'delete' in request.POST:
            tarea = Tarea.objects.get(pk=request.POST.get('delete'))
            tarea.delete()
            return redirect(request.path)
        
        elif 'edit' in request.POST:
            return redirect('tareas:tareaEdit',pk = request.POST.get('edit'))
        
    context = {}

    form = TareasFormExtended()
    tareas = Tarea.objects.all()

    context['form'] = form
    context['tareas'] = tareas

    return render(request,'tareas/home.html',context)



def detail_tarea(request,pk):
    tarea = Tarea.objects.get(pk = pk)
    return render(request,'tareas/detail-tarea.html',{'tarea':tarea})

def edit_tarea(request,pk):
    tarea = Tarea.objects.get(pk = pk)
    form = TareasFormExtended(request.POST or None, instance=tarea)
    if form.is_valid():
        form.save()
        return redirect('tareas:home')
    
    return render(request,'tareas/edit_tarea.html',{'form':form})
