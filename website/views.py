from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages

from contact.forms import ContactForm


class NomadPageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(NomadPageView, self).get_context_data(**kwargs)
        return context

def contact(request):
    ctxt = dict()
    template = 'contact.html'
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We will contact you shortly.")
            return redirect('home')

        # Show system error msg
        messages.error(request, "You must complete all required fields")
    ctxt['form'] = form
    return render(request, template, ctxt)

