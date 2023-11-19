import string

from captcha.image import ImageCaptcha
from django.shortcuts import render, redirect
from random import choice
from first_ukraine.models import User

"""
RuntimeError: Model class ukraine.models.user.User doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
add 'ukraine.models' in settings under "INSTALLED_APPS"
"""
FT = ["False", "True"]


def register_view(request):
    if 'email' in request.GET:
        form_not_complete = {'error': 'Empty field'}
        for k in request.GET.values():
            if k is None:
                return render(request, 'register.html', form_not_complete)
        if request.GET['password'] != request.GET['confirmPassword']:
            error_pwd = {'error': 'Password does not match'}
            return render(request, 'register.html', error_pwd)
        if request.GET['captcha_id'][::-1] != request.GET['captcha_value']:
            captcha_error = {'captcha_error': 'Captcha does not match'}
            return render(request, 'register.html', captcha_error)
        newUser = User(firstname=request.GET['firstname'],
                       lastname=request.GET['lastname'],
                       country=request.GET['country'],
                       email=request.GET['email'],
                       phone=request.GET['phone'],
                       owner=FT.index(request.GET['owner']),
                       password=request.GET['password'],
                       gender=request.GET['gender'])

        newUser.save()
        return redirect('/login')
    else:
        letters = string.ascii_lowercase
        letters.join(string.digits)
        result_str = ''.join(choice(letters) for _ in range(4))
        image = ImageCaptcha()
        value = {'result_str': result_str}
        image.write(result_str, 'first_ukraine/static/generated_captcha/captcha.jpg')
        return render(request, 'register.html', value)
