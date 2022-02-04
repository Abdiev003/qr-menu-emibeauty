import imp
from django.views.generic import ListView

from core.models import Service, ServiceItem


class HomeListView(ListView):
    template_name = 'index.html'
    queryset = Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)
        context['service_items'] = ServiceItem.objects.filter(is_active=True)

        return context
