from django.shortcuts import render
from django.utils import timezone

def current_time(request):
    # Get the current time in the configured time zone
    current_time = timezone.now()
    return render(request, 'current_time.html', {'current_time': current_time})
