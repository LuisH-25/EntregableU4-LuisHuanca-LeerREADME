from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import Portafolio
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PortafolioForm
from django.utils import timezone
import urllib.request
import datetime
import json

class PortafolioView(LoginRequiredMixin, TemplateView):
    template_name = "portafolio/index.html"
    extra_context = {"portafolios": Portafolio.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Portafolios"] = Portafolio.objects.all()
        context["hora_actual"] = timezone.localtime
        return context

class PortafolioCreate(LoginRequiredMixin, FormView):
    model = Portafolio
    template_name = "portafolio/create.html"
    form_class = PortafolioForm

    def form_valid(self, form):
        Portafolio.objects.create(**form.cleaned_data)
        return redirect("index")


@login_required
def deletePortafolio(request, id):
    portafolio = Portafolio.objects.get(id=id)
    portafolio.delete()
    return redirect("index")