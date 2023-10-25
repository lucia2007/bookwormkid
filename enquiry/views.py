from django.shortcuts import (

                              render,
                              get_object_or_404,
                              redirect)
from django.urls import reverse
from .models import Enquiry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EnquiryForm


def all_enquiries(request):
    """ A view to return all enquiries """
    if request.user.is_superuser:
        enquiries = Enquiry.objects.all().filter
    else:
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
        messages.error(
                       request,
                       'Sorry, only store owner can add new enquiries.'
                       )
        return redirect(reverse('home'))

    enquiries = Enquiry.objects.all()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
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


@login_required
def edit_enquiry(request, enquiry_id):
    """ Edit an enquiry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can edit enquiries.')
        return redirect(reverse('home'))

    enquiry = get_object_or_404(Enquiry, pk=enquiry_id)

    if request.method == 'POST':
        form = EnquiryForm(request.POST, instance=enquiry)

        if form.is_valid():
            form.save()
            messages.success(request, "Enquiry was edited successfully.")
            return redirect(reverse('enquiries'))
        else:
            messages.error(request,
                           'Enquiry was not edited. Correct the form inputs.'
                           )
    else:
        form = EnquiryForm(instance=enquiry)

    template = 'enquiry/edit_enquiry.html'
    context = {
        'form': form,
        'enquiry': enquiry,
        'on_page': True,
    }

    return render(request, template, context)


@login_required
def delete_enquiry(request, enquiry_id):
    """ Delete an enquiry """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only the admin can delete enquiries.')
        return redirect(reverse('enquiries'))

    enquiry = get_object_or_404(Enquiry, pk=enquiry_id)
    enquiry.delete()
    messages.success(request,
                     'Enquiry was deleted successfully.')

    context = {
        'on_page': True,
    }

    return redirect(reverse('enquiries'), context)
