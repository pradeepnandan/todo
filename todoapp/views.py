from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import ToDoForms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView

# Create your views here.
def home(request):

    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        remarks=request.POST.get('remarks','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority, remarks=remarks,date=date)
        task.save()
    task = Task.objects.all()
    return render(request,'home.html',{'task1':task})
# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})
def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=ToDoForms(request.POST or None,instance=task )
    if f.is_valid():
        f.save()
        return redirect ('/')
    return render(request,'edit.html',{'f':f,'task':task})
class Tasklistview(ListView):
    model = Task
    template_name = 'cbvhome.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'cbvdetails.html'
    context_object_name = 'task2'
class  TaskUpdateView(UpdateView):
    model = Task
    template_name = 'cbvEdit.html'
    context_object_name = 'task'
    fields = ('name','priority','date','remarks')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'cbvDelete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')
