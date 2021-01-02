import form as form
from django.shortcuts import render
from django.views.generic import ListView

from .forms import FilterForm

from .models import FilterChoices
import json
from . import models
from django.views import generic


# Create your views here.


def home(request):
    db_choices = FilterChoices.objects.all()[0]
    if (request.method == "GET"):
        jsonDec = json.decoder.JSONDecoder()
        choices_company = [(i, i) for i in jsonDec.decode(db_choices.company)]
        choices_product = [(i, i) for i in jsonDec.decode(db_choices.product)]
        choices_parameter = [(i, i) for i in jsonDec.decode(db_choices.parameter)]

        form = FilterForm(choices_company=choices_company, choices_product=choices_product,
                          choices_parameter=choices_parameter)

        return render(request, "comparison/home.html", {'form': form})

    if request.method == "POST" and 'submit' in request.POST:
        form_company = request.POST["Company"] or None
        form_product = request.POST["Product"] or None
        form_parameter = request.POST["Parameter"] or None
        return render(request, "comparison/comparison.html",
                      {'form_company': form_company, 'form_product': form_product, 'form_parameter': form_parameter})


def compare(request):
    pass
