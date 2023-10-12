from django.shortcuts import (

                              render,
                              get_object_or_404,
                              reverse,
                              redirect)
from django.urls import reverse_lazy
from .models import Enquiry
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EnquiryForm


def all_enquiries(request):
    """ A view to return all enquiries """
    enquiries = Enquiry.objects.all().filter(status=1)

    context = {
        'enquiries': enquiries,
        'on_page': True,
    }

    return render(request, 'enquiry/enquiries.html', context)


@login_required
def add_enquiry(request):
    """ Add a new enquiry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can add new enquiries.')
        return redirect(reverse('home'))

    enquiries = Enquiry.objects.all()
    print("I'm a superuser.")

    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        print(enquiries)

        if form.is_valid():
            print('inside the form valid function')
            form.save()
            print('i am saved')
            messages.success(request, "Enquiry was added successfully.")
            return redirect(reverse('enquiries'))
        else:
            messages.error(request,
                           'Enquiry was not added. Correct the form inputs.'
                           )
    else:
        form = EnquiryForm()

    template = 'enquiry/add_enquiry.html'
    context = {
        'form': form,
        'enquiries': enquiries,
        'on_page': True,
    }

    return render(request, template, context)
