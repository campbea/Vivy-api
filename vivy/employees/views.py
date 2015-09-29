from django.views.generic import TemplateView

from .models import Employee


class EmployeeDashboardView(TemplateView):
    template_name = "employee-dash.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDashboardView, self).get_context_data(**kwargs)
        context['projects'] = Employee.objects.all()
        return context
