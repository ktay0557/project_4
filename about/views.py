from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm

# Create your views here.


def about_me(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your enquiry has been submitted. We aim to respond within 3 working days'
            )

    about = About.objects.all().order_by("-edited_on").first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )
