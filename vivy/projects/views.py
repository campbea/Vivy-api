from django.views.generic import TemplateView

from .models import Project


class ProjectDashboardView(TemplateView):
    template_name = "project-dash.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDashboardView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
