from django import forms
from django.shortcuts import render, redirect

from first_ukraine.models import Establishment, User

class EstablishmentForm(forms.Form):
    name = forms.CharField(max_length=50)
    HOTEL = "HO"
    CAFE = "CA"
    RESTAURANT = "RE"
    choices = [(HOTEL, "Hotel"), (CAFE, "Cafe"), (RESTAURANT, "Restaurant")]
    establishment_type = forms.ChoiceField(choices=choices, required=True)
    capacity = forms.IntegerField()
    covid_hygiene = forms.BooleanField(required=False)


def register_establishment(request):
    if request.GET:
        if request.GET['name'] is not None and request.GET['capacity'] is not None:
            owner = User.objects.filter(id=request.session['id'])[0]
            establishment = Establishment(name=request.GET['name'],
                                          establishment_type=request.GET['establishment_type'],
                                          capacity=request.GET['capacity'],
                                          covid_hygiene='covid_hygiene' in request.GET,
                                          owner=owner)
            establishment.save()
            return redirect("/welcome")
        else:
            error_context = {"error_form": "An error have appeared"}
            return render(request, "owner_form.html", error_context)
    establishment_form = {'establishmentForm': EstablishmentForm()}
    return render(request, "owner_form.html", establishment_form)
