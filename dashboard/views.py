from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Computer

class PCMonitorView(generic.ListView):
    template_name = 'dashboard/pcmonitor.html'
    context_object_name = 'computer_list'
    
    def get_queryset(self):
        return Computer.objects.order_by('type')
