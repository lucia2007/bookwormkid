from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


#  https://github.com/davidcalikes/sensical.ie/blob/main/sensical/urls.py
def error_view(request):
    """ 500 Internal Server Error """
    return render(request, "500.html", status=500)


def error_view_403(request, exception):
    """ 403 Unauthorized Action """
    return render(request, "403.html", status=403)
