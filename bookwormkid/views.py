from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


def handler403(request, exception):
    """ Rendering 403 and 500 error pages """
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        # Handle unexpected erros with a generic 500 error page
        return render(request, '500.html', status=500)
