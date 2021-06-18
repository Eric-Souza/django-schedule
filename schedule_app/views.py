from django.shortcuts import render
from .models import Event


def list_events(request):
    event = Event.objects.all()
    data = {'events': event}

    return render(request, 'schedule.html', data)
