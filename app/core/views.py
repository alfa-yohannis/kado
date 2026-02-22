from django.shortcuts import render
from .models import Counter

def index(request):
    counter, _ = Counter.objects.get_or_create(id=1)
    return render(request, 'index.html', {'counter': counter})

def increment_value(request):
    if request.method == "POST":
        counter, _ = Counter.objects.get_or_create(id=1)
        counter.increment()
        # We render ONLY the partial file, not the whole page
        return render(request, 'partials/counter_display.html', {'counter': counter})