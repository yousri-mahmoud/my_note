from django.shortcuts import render , get_object_or_404 , redirect
from .models import Note
from .forms import NoteForm
# Create your views here.


def index (request):
    notes = Note.objects.order_by('-pub_date')
    context = {'notes': notes}
    return render (request ,'index.html',context )

def detail(request, note_id):
    note =  get_object_or_404(Note , id=note_id)
    context = {'note': note}
    return render(request , 'detail.html' , context)


def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm()

    context = {'form' : form}

    return render(request, 'add.html', context)




def edit(request , note_id):
    note =  get_object_or_404(Note , id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST , instance =note)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm(instance =note)

    context = {'form' : form}

    return render(request, 'add.html', context)


def delete(request , note_id):
    dele_note = Note.objects.get(pk=note_id).delete()
    return redirect('/')
