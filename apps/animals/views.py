from multiprocessing import context
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


from .models import Animal
from .forms import AnimalForm


class IndexView(generic.ListView):
    model = Animal
    template_name = 'animals/index.html'
    context_object_name = 'animales'
    queryset = model.objects.all()
    
    # def get_queryset(self):
    #     return self.model.objects.filter(edad=2)

class CreateView(generic.CreateView):
    model = Animal
    template_name = 'animals/create.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animals:index')
    
    def post(self, request, *args, **kwargs):
        # Lógica para guardar al animal
        return super().post(request, *args, **kwargs)
    

    
class UpdateView(generic.UpdateView):
    model = Animal
    template_name = 'animals/create.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animals:index')

    
class DeleteView(generic.DeleteView):
    model = Animal
    # template_name = 'animals/delete.html'
    success_url = reverse_lazy('animals:index')
    
class DetailView(generic.DetailView):
    model = Animal
    template_name = 'animals/detail.html'
    context_object_name = 'animal'
