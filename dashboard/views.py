from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Computer

class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'computer_list'
    
    def get_queryset(self):
        return Computer.objects.order_by('type')

class DetailView(generic.DetailView):
    template_name = 'dashboard/detail.html'
    model = Computer