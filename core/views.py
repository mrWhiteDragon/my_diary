from django.shortcuts import render
from .models import Note

def main(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        Note.objects.create(title=title, text=text)

    notes = Note.objects.all().order_by('-date_time')
    return render(request, 'main.html', {'notes': notes})
