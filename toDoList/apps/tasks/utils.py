from django.http import HttpResponse


def is_authorized(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        else:
            return HttpResponse('Not authorized', status=401)
    return wrapper
