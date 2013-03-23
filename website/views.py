from django.views.generic.base import TemplateView


class NomadPageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(NomadPageView, self).get_context_data(**kwargs)
        return context

