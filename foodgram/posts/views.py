"""Posts views"""
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

posts = [
    {
        'title' : 'Mont Blac',
        'user' : {
            'name' : 'Jessica Sánchez',
            'picture' : 'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/600/400/?image=1036',

    },
    {
        'title' : 'Via  Láctea',
        'user' : {
            'name' : 'Marco Fuentes',
            'picture' : 'https://picsum.photos/60/60/?image=1005',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/600/600/?image=903',

    },
    {
        'title' : 'Nuevo auditorio',
        'user' : {
            'name' : 'Tatiana Fuentes',
            'picture' : 'https://picsum.photos/60/60/?image=1014',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/500/700/?image=1076',

    }
]


@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts':posts})