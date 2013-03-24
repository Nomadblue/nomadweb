from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from propaganda.models import Subscriber

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
        messages.error(request, "You must complete all required fields")
    ctxt['form'] = form
    return render(request, template, ctxt)


class SubscriberCreateView(CreateView):
    model = Subscriber
    template_name = 'subscriber_form.html'
    success_url = reverse_lazy('home')

