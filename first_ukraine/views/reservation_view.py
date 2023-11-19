from django import forms
from django.shortcuts import render

from first_ukraine.models import Reservation, Establishment, User


class Reservation_form(forms.Form):
    from_date = forms.DateField(required=True)
    to_date = forms.DateField(required=True)
    number_of_person = forms.IntegerField(required=True)


def register_reservation(request, establishment_id):
    if request.GET:
        from_filter = Reservation.objects.filter(from_date__lte=request.GET['to_date'])
        to_filter = from_filter.filter(to_date__gte=request.GET['from_date'])
        persons = 0
        establishment = Establishment.objects.filter(id=establishment_id)[0]
        for reservation in to_filter:
            persons += reservation.number_of_person
        if persons + int(request.GET['number_of_person']) > establishment.capacity:
            context = {"reservationForm": Reservation_form(),
                       "establishment_id": establishment_id,
                       "sorry": "Not enough Place"}
            return render(request, "reservation.html", context)
        reservation = Reservation(establishment=establishment,
                                  user=User.objects.filter(id=request.session['id'])[0],
                                  from_date=request.GET['from_date'],
                                  to_date=request.GET['to_date'],
                                  number_of_person=request.GET['number_of_person'])
        reservation.save()
        return render(request, "welcome.html")
    else:
        context = {"reservationForm": Reservation_form(),
                   "establishment_id": establishment_id}
        return render(request, "reservation.html", context)
