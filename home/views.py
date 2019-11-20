from django.shortcuts import render, redirect
from .forms import ContactForm, NewsletterForm
from .models import Contact
from songs.models import Songs

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact(request):
    all_contacts = Contact.objects.all()
    lsong_1 = Songs.objects.get(id=1)
    lsong_2 = Songs.objects.get(id=2)
    lsong_3 = Songs.objects.get(id=3)
    lsong_4 = Songs.objects.get(id=4)
    if request.method == "POST":
        c_form = ContactForm(request.POST)
        n_form = NewsletterForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('contact')
        elif n_form.is_valid():
            n_form.save()
            return redirect('contact')
    else:
        c_form = ContactForm()
        n_form = NewsletterForm()
        
    context = {
        'c_form': c_form,
        'n_form': n_form,
        'all_contact': all_contacts,
        'lsong_1': lsong_1,
        'lsong_2': lsong_2,
        'lsong_3': lsong_3,
        'lsong_4': lsong_4,
    }
    return render(request, 'contact.html', context)