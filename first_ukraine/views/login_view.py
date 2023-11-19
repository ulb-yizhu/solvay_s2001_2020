from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from first_ukraine.models import User


def login_view(request):
    # if form sent
    #   if inputs bad
    #     render
    #   else
    #     redirect
    # else
    #    render empty
    if 'email' in request.GET and 'password' in request.GET:
        enteredEmail = request.GET['email']
        enteredPassword = request.GET['password']
        if len(User.objects.filter(email=enteredEmail).filter(password=enteredPassword)) == 1:
            user = User.objects.filter(email=enteredEmail).filter(password=enteredPassword)[0]
            request.session['id'] = user.id
            request.session['owner'] = user.owner
            return redirect("/welcome")
        else:
            login_error = {'login_error': 'Bad login or password'}
            return render(request, 'login.html', login_error)
    else:
        return render(request, 'login.html')
