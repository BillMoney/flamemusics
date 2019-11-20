from django.shortcuts import render, redirect
from .models import Songs
from django.http import Http404
from home.models import Contact
from home.forms import NewsletterForm
from django.db.models import Q
# Create your views here.

def songs(request):
    query = request.GET.get('search')
    all_contacts = Contact.objects.all()
    lsong_1 = Songs.objects.get(id=1)
    lsong_2 = Songs.objects.get(id=2)
    lsong_3 = Songs.objects.get(id=3)
    lsong_4 = Songs.objects.get(id=4)
    all_songs = Songs.objects.all().order_by('-date_published')
    
    if request.method == "POST":
        n_form = NewsletterForm(request.POST)
        if n_form.is_valid():
            n_form.save()
            return redirect('songs')
    
    else:
        n_form = NewsletterForm()

    error_message = ''
    if query:
        error_message = ''
        all_songs = Songs.objects.filter(
            Q(song_title__icontains=query)|
            Q(artist__icontains=query) |
            Q(date_published__icontains=query)
        )

        if query != all_songs:
            error_message = 'error'

    context = {
        'error_message': error_message,
        'all_songs': all_songs,
        'search': query,
        'lsong_1': lsong_1,
        'lsong_2': lsong_2,
        'all_contact': all_contacts,
        'lsong_3': lsong_3,
        'lsong_4': lsong_4,
        'n_form': n_form,
    }
    return render(request, 'download.html', context)

def preview(request, pk):
    all_contacts = Contact.objects.all()
    lsong_1 = Songs.objects.get(id=1)
    lsong_2 = Songs.objects.get(id=2)
    lsong_3 = Songs.objects.get(id=3)
    lsong_4 = Songs.objects.get(id=4)
    try:
        song = Songs.objects.get(id=pk)
    except Songs.DoesNotExist:
        raise Http404('It does not exist')
    context = {
        'song': song,
        'lsong_1': lsong_1,
        'lsong_2': lsong_2,
        'all_contact': all_contacts,
        'lsong_3': lsong_3,
        'lsong_4': lsong_4,
    }
    return render(request, 'preview.html', context)