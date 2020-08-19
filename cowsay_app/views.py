from django.shortcuts import render, HttpResponseRedirect, reverse
import subprocess
from django.shortcuts import render
from cowsay_app.models import CowMessages
from cowsay_app.forms import PrintMessageForm


# Create your views here.


def index_view(request):
    # https://stackoverflow.com/questions/40586992/keep-html-formatting-when-passing-variable-from-django-template-to-view
    if request.method == "POST":
        form = PrintMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowMessages.objects.create(
                text=data.get("text"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = PrintMessageForm()
    Message = CowMessages.objects.all().last()
    output = subprocess.run(
        ["cowsay", f'{Message}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return render(request, "index.html", {"form": form, "display": output.stdout})


def previous_view(request):
    # https://stackoverflow.com/questions/47428403/how-to-get-the-last-10-item-data-in-django

    ranks = CowMessages.objects.all().order_by('-id')[:10]

    return render(request, "previous.html", {"top10": ranks},)
