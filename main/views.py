from django.shortcuts import render, redirect

from .forms import ThingToDoForm
from .models import ThingToDo
from django.contrib import messages


# Create your views here.
def homepage(request):
    if request.method == "POST":
        form = ThingToDoForm(data=request.POST)
        if form.is_valid():
            thing_to_do = form.save()
            messages.success(request, f"New activity added!")
        else:
            messages.error(request, f"The activity is already there!")
    form = ThingToDoForm()

    return render(request,
                  'main/homepage.html',
                  context={'form': form,
                           'things_to_do': ThingToDo.objects.all().order_by("-date")})


def delete_entry(request, id):
    ThingToDo.objects.get(id=id).delete()
    messages.error(request, f"Activity was not finished!")

    return redirect('main:homepage')


def delete_all(request):
    ThingToDo.objects.all().delete()
    messages.error(request, f"Activities deleted!")

    return redirect('main:homepage')


def update_entry(request, id):
    edit = ThingToDo.objects.get(id=id)

    if request.method == "POST":
        form = ThingToDoForm(data=request.POST)
        if form.is_valid():
            edit.activity_text = request.POST.get('activity_text')
            edit.save()
            messages.success(request, f"Activity updated!")

            return redirect('main:homepage')

        else:
            messages.error(request, f"The activity is already there!")

    form = ThingToDoForm()

    return render(request,
                  'main/update.html',
                  context={'form': form})


def finish_entry(request, id):
    ThingToDo.objects.get(id=id).delete()
    messages.success(request, f"Activity was finished! Congratulations!")

    return redirect('main:homepage')