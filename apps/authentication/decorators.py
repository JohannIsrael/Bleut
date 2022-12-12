from django.shortcuts import redirect


def val_authentication(funtion):

    def wrap(request, *args, **kwargs):

        if request.user.is_anonymous:
            return redirect('home')

        return function(request, *args, **kwargs)

    return wrap