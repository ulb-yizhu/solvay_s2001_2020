from django.shortcuts import render

from first_ukraine.models import Establishment


def welcome_view(request):
    if request.GET:
        establishments = Establishment.objects.filter(name__contains=request.GET['establishmentName'])
        if 'covid' in request.GET:
            establishments = establishments.filter(covid_hygiene=True)
        else:
            establishments = establishments.filter(covid_hygiene=False)
        context = {"establishments": establishments, "context_owner": request.session['owner']}
        return render(request, 'welcome.html', context)
    else:
        context = {"context_owner": request.session['owner']}
    return render(request, 'welcome.html', context)
