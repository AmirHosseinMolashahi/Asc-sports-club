from django.views.generic import TemplateView

# Create your views here.

class DashboardPage(TemplateView):
    template_name = 'dashboard/dashboard.html'